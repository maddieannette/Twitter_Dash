from dash import Dash, dash_table
import pandas as pd

trends = pd.read_csv('Trends_File10_21_22.csv')

app = Dash(__name__)

app.layout = dash_table.DataTable(trends.to_dict('records'), [{"name": i, "id": i} for i in trends.columns])

if __name__ == '__main__':
    app.run_server(debug=True)