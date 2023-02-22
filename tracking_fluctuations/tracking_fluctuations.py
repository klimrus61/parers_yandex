import gspread


class TrackingFluctuations():
    """
    
    """
    def __init__(self, key: str, cred_file_path: str) -> None:
        self.CREDENTIALS_FILE = cred_file_path  # имя файла с закрытым ключом
        self.gc = gspread.service_account(filename=self.CREDENTIALS_FILE)
        self.sh = self.gc.open_by_key(key)
        self.actual_worksheet = self.sh.get_worksheet(2)
        self.sum_cells = 0

    def _get_average_sum(self, tracked_cell, user_name, app_name) -> int:
        '''
        Получаем среднюю сумму за предыдущие 7 дней. 
        '''
        average_previous_seven_days_sum = 0
        last_seven_days_values = []
        row_values = self.actual_worksheet.row_values(tracked_cell.row)
        yesterday = tracked_cell.col - 2 - 1
        for col_index in range(yesterday, 1, -2):
            if not row_values[col_index]:
                last_seven_days_values.append(0)
            else:
                last_seven_days_values.append(
                    float(row_values[col_index].replace(',', '.')))

        previous_worksheet_index = self.actual_worksheet.index - 1
        actual_param_name = row_values[1]

        while previous_worksheet_index >= 0 and len(last_seven_days_values) < 7:
            worksheet = self.sh.get_worksheet(previous_worksheet_index)
            user_and_app_names = worksheet.col_values(1)
            if user_name not in user_and_app_names or app_name not in user_and_app_names:
                break
            app_name_cell = worksheet.find(app_name)
            param_names = worksheet.col_values(2)
            actual_row_index = None
            for row_index in range(app_name_cell.row-1, app_name_cell.row + 5):
                if param_names[row_index] == actual_param_name:
                    actual_row_index = row_index
                    break
            worksheet_row_values = worksheet.row_values(actual_row_index)
            start_col = 15 - (tracked_cell.col % 2)
            for col_index in range(start_col, 1, -2):
                if len(last_seven_days_values) == 7:
                    break
                if not worksheet_row_values[col_index]:
                    last_seven_days_values.append(0)
                else:
                    last_seven_days_values.append(
                        float(row_values[col_index].replace(',', '.')))
            previous_worksheet_index += -1
        count_days_of_week_with_values = sum((1 for day_value in last_seven_days_values if day_value != 0))
        if count_days_of_week_with_values > 0:
            average_previous_seven_days_sum = sum(last_seven_days_values) / count_days_of_week_with_values
        return average_previous_seven_days_sum

    def _average_difference_check(self, tracked_cell, user_name, app_name):
        ''' Сравнение  суммы из результатов парсинга и среднего значения за неделю.
       Если разница отличается на 10% ячейка изменяется ячейку
        '''
        if tracked_cell.value:
            tracked_cell_value = float(tracked_cell.value.replace(',', '.'))
        else:
            return self.sum_cells

        average_weekly_sum = self._get_average_sum(
            tracked_cell, user_name, app_name)
        if tracked_cell_value > average_weekly_sum * 1.1 and average_weekly_sum > 0:
            self.actual_worksheet.format(tracked_cell.address,
                                         {"backgroundColor": {
                                             "red": 0.0,
                                             "green": 55.0,
                                             "blue": 0.0
                                         }, })
            self.sum_cells += 1
        elif tracked_cell_value < average_weekly_sum * 0.9 and average_weekly_sum > 0:
            self.actual_worksheet.format(tracked_cell.address,
                                         {"backgroundColor": {
                                             "red": 55.0,
                                             "green": 0.0,
                                             "blue": 0.0
                                         }, })
            self.sum_cells += 1
        return self.sum_cells


if __name__ == "__main__":

    SHEET_URL = '1ZRMLXTClSNypxb3Lk_LkEYBAwDrnqD3-opeMwiOJ0AQ'
    CRED = 'tracking_fluctuations\cred.json'

    tracking_fluctuation = TrackingFluctuations(
        key='1ZRMLXTClSNypxb3Lk_LkEYBAwDrnqD3-opeMwiOJ0AQ', cred_file_path=CRED)
    # for param_row in range(3, 13):
    #     print(tracking_fluctuation._average_difference_check(tracking_fluctuation.actual_worksheet.cell(param_row, 9), 'Аккаунт 1', 'Название игры 1'))
    tracking_fluctuation.actual_worksheet = tracking_fluctuation.sh.get_worksheet(1)
    print(tracking_fluctuation._average_difference_check(tracking_fluctuation.actual_worksheet.acell('D34'), 'Аккаунт 1', 'Название игры 6'))
