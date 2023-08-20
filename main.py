import tkinter as tk
import historyChart as histChart
import candlestickChart as candChart

class GraphInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Acompanhamento e Visualização de Preços do Bitcoin")
        
        self.hist_button = tk.Button(root, text="Gráfico de Histórico de 5 anos", command=self.create_history_graph)
        self.hist_button.pack(pady=10)
        
        self.candle_button = tk.Button(root, text="Gráfico de Candlestick de 30 dias", command=self.create_candlestick_chart)
        self.candle_button.pack(pady=10)
        
    def create_history_graph(self):
        histChart.createHistoryGraph()
    
    def create_candlestick_chart(self):
        candChart.createCandlestickChart()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x100")
    app = GraphInterface(root)
    root.mainloop()