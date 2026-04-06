import pandas as pd
import numpy as np

from lightgbm import LGBMRegressor


def cargar_datos():
    X_train = pd.read_csv("X_train_final.csv")
    X_val = pd.read_csv("X_val_final.csv")
    y_train = pd.read_csv("y_train.csv").squeeze("columns")
    y_val = pd.read_csv("y_val.csv").squeeze("columns")

    return X_train, X_val, y_train, y_val


def entrenar_modelo(X_train, y_train):
    model = LGBMRegressor(
        n_estimators=500,
        learning_rate=0.05,
        random_state=42
    )

    model.fit(X_train, y_train)
    return model


def predecir(model, X_val):
    y_pred = model.predict(X_val)
    return y_pred


def calcular_metricas(y_val, y_pred):
    from sklearn.metrics import mean_absolute_error

    y_val_real = np.expm1(y_val)
    y_pred_real = np.expm1(y_pred)

    mae = mean_absolute_error(y_val_real, y_pred_real)

    print("MAE (escala real):", round(mae, 2))

    return y_val_real, y_pred_real


def simular_pricing(y_val_real, y_pred_real):
    margen = 0.30

    premium = y_pred_real * (1 + margen)
    profit = premium - y_val_real

    print("Profit promedio:", round(profit.mean(), 2))
    print("Profit total:", round(profit.sum(), 2))

    return premium, profit


def ejecutar_pipeline():
    print("Cargando datos...")
    X_train, X_val, y_train, y_val = cargar_datos()

    print("Entrenando modelo...")
    model = entrenar_modelo(X_train, y_train)

    print("Generando predicciones...")
    y_pred = predecir(model, X_val)

    print("Calculando métricas...")
    y_val_real, y_pred_real = calcular_metricas(y_val, y_pred)

    print("Simulando pricing...")
    premium, profit = simular_pricing(y_val_real, y_pred_real)

    print("Pipeline completado.")


if __name__ == "__main__":
    ejecutar_pipeline()