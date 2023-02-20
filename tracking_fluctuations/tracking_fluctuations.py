import gspread


SHEET_URL = '1ZRMLXTClSNypxb3Lk_LkEYBAwDrnqD3-opeMwiOJ0AQ'
CRED = 'cred.json'


class TrackingFluctuations():

    def __init__(self, key: str, cred_file_path: str ) -> None:
        self.CREDENTIALS_FILE = cred_file_path  # имя файла с закрытым ключом
        self.gc = gspread.service_account(filename=self.CREDENTIALS_FILE)
        self.sh = self.gc.open_by_key(key)
        self.actual_worksheet = self.sh.get_worksheet(0)
        self.sum_cells = 0


    def catch_fluctuations(self, tracked_cell):

         
        if tracked_cell.value:
            tracked_cell_value = float(tracked_cell.value.replace(',', '.'))
        else:
            return self.sum_cells
        average_weekly_value = 0
        numerator = 0
        denominator = 0

        previous_days = self.actual_worksheet.row_values(tracked_cell.row)
        for i in range(tracked_cell.col -2, 1, -2):
            if not previous_days[i]:
                continue
            numerator += float(previous_days[i].replace(',', '.'))
            denominator += 1

        if denominator != 0:
            average_weekly_value = numerator / denominator
            print(tracked_cell_value / average_weekly_value)
            print(tracked_cell_value, average_weekly_value)
        if tracked_cell_value > average_weekly_value * 1.1 and average_weekly_value > 0:
            self.actual_worksheet.format(tracked_cell.address,
            {"backgroundColor": {
                    "red": 0.0,
                    "green": 55.0,
                    "blue": 0.0
            },})
            self.sum_cells += 1
        elif tracked_cell_value < average_weekly_value * 0.9 and average_weekly_value > 0:
            self.actual_worksheet.format(tracked_cell.address,
            {"backgroundColor": {
                    "red": 55.0,
                    "green": 0.0,
                    "blue": 0.0
            },})
            self.sum_cells += 1
        return self.sum_cells






t = TrackingFluctuations(key=SHEET_URL, cred_file_path=CRED)
for i in range(3, 17):
    print(t.catch_fluctuations(t.actual_worksheet.cell(40, i)))