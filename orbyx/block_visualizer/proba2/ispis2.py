from services.visualizer_api import Visualizer


class Ispis(Visualizer):
    def visualize(self, proba):
        print(proba)
        return proba
