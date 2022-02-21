

from sklearn.pipeline import Pipeline
from joblib import dump
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def update_model(model: Pipeline):
    dump(model, '/Users/mayel/fixdesktop/virtual/deploy_ml_fundamentals/models/model.pkl')
    return None


def save_simple_metrics_report(train_score: float, test_score: float, validation_score: float, model: Pipeline):
    with open('report.txt', 'w') as report_file:
        report_file.write('# Model Pipeline Description')

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}: {value.__repr__()}\n')

        report_file.write(f'### Train Score : {train_score}')
        report_file.write(f'### Test Score : {test_score}')
        report_file.write(f'### Validation Score : {validation_score}')

    return None


def get_model_performance_test_set(y_real: pd.Series, y_pred: pd.Series):
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figheight(8)
    sns.regplot(x=y_pred, y=y_real, ax=ax)
    ax.set_xlabel('Predicted Worldwide Gross')
    ax.set_ylabel('Real Worldwide Gross')
    ax.set_title('R2 Behavior of model prediction')
    fig.savefig('model_performance.png')
    return None
