import gspread


class TrackingFluctuations():

    def __init__(self, key: str, cred_file_path: str ) -> None:
        self.CREDENTIALS_FILE = cred_file_path  # имя файла с закрытым ключом
        self.gc = gspread.service_account(filename=self.CREDENTIALS_FILE)
        self.sh = self.gc.open_by_key(key)
        self.actual_worksheet = self.sh.get_worksheet(2)
        self.sum_cells = 0
        
        self.ids_of_required_rows_for_worksheets = ['' for _ in range(len(self.sh.worksheets()))] # self.ids_of_required_rows[i] = нужная строка на i-том листе

        
    def get_last_seven_days_average_sum(self, tracked_cell, user_name: str, app_name: str) -> int:

        average_previous_seven_days_sum = 0
        last_seven_days_values = []
        
        previous_days = self.actual_worksheet.row_values(tracked_cell.row)
        yesterday = tracked_cell.col - 2 - 1
        for col_index in range(yesterday, 1, -2):
            if not previous_days[col_index]:
                continue
            last_seven_days_values.append(float(previous_days[col_index].replace(',', '.')))

        previous_worksheet_index = self.actual_worksheet.index - 1

        if len(last_seven_days_values) < 7:
            while previous_worksheet_index >= 0 and len(last_seven_days_values) < 7:
                worksheet = self.sh.get_worksheet(previous_worksheet_index)
                user_and_app_names = worksheet.col_values(1)
                if user_name not in user_and_app_names or app_name not in user_and_app_names:
                    break
                row_value = self.ids_of_required_rows_for_worksheets[previous_worksheet_index]
                if not row_value:
                    row_value = tracked_cell.row
                worksheet_row_values = worksheet.row_values(row_value)
                start_col = 15 - (tracked_cell.col % 2)
                for col_index in range(start_col, 1, -2):
                    if len(last_seven_days_values) == 7:
                        break
                    if not worksheet_row_values[col_index]:
                        continue
                    last_seven_days_values.append(float(previous_days[col_index].replace(',', '.')))
                previous_worksheet_index += -1
        if len(last_seven_days_values) > 0:
            average_previous_seven_days_sum = sum(last_seven_days_values) / len(last_seven_days_values)
        return average_previous_seven_days_sum

                
    def catch_fluctuations(self, tracked_cell, user_name, app_name):

        if tracked_cell.value:
            tracked_cell_value = float(tracked_cell.value.replace(',', '.'))
        else:
            return self.sum_cells

        average_weekly_sum = self.get_last_seven_days_average_sum(tracked_cell, user_name, app_name)
        
            
        if tracked_cell_value > average_weekly_sum * 1.1 and average_weekly_sum > 0:
            self.actual_worksheet.format(tracked_cell.address,
            {"backgroundColor": {
                    "red": 0.0,
                    "green": 55.0,
                    "blue": 0.0
            },})
            self.sum_cells += 1
        elif tracked_cell_value < average_weekly_sum * 0.9 and average_weekly_sum > 0:
            self.actual_worksheet.format(tracked_cell.address,
            {"backgroundColor": {
                    "red": 55.0,
                    "green": 0.0,
                    "blue": 0.0
            },})
            self.sum_cells += 1
        return self.sum_cells





if __name__ == "__main__":
    
    SHEET_URL = '1ZRMLXTClSNypxb3Lk_LkEYBAwDrnqD3-opeMwiOJ0AQ'
    CRED = 'tracking_fluctuations\cred.json'

    tracking_fluctuation = TrackingFluctuations(key='1ZRMLXTClSNypxb3Lk_LkEYBAwDrnqD3-opeMwiOJ0AQ', cred_file_path=CRED)
    # for param_row in range(25, 35):
    #     print(tracking_fluctuation.catch_fluctuations(tracking_fluctuation.actual_worksheet.cell(param_row, 4), 'Аккаунт 1', 'Название игры 1'))

    print(tracking_fluctuation.catch_fluctuations(tracking_fluctuation.actual_worksheet.acell('O39'), 'Аккаунт 1', 'Название игры 1'))