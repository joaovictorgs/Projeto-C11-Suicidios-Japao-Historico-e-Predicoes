import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from data_processing import process_japan_data


def analyze_japan_decomposition():
    df_japan = process_japan_data('data/combined_processed_data.csv')
    
    df_japan['Year'] = pd.to_datetime(df_japan['Year'], format='%Y')
    df_japan.set_index('Year', inplace=True)
    
    series = df_japan['No of Suicides']
    
    decomposition = seasonal_decompose(series, model='additive', period=12)
    
    fig, axes = plt.subplots(4, 1, figsize=(14, 10))
    
    decomposition.observed.plot(ax=axes[0], color='#2c3e50')
    axes[0].set_ylabel('Observado', fontsize=12)
    axes[0].set_title('Decomposição da Série Temporal - Suicídios no Japão', fontsize=15, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    decomposition.trend.plot(ax=axes[1], color='#e74c3c')
    axes[1].set_ylabel('Tendência', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    
    decomposition.seasonal.plot(ax=axes[2], color='#3498db')
    axes[2].set_ylabel('Sazonalidade', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    
    decomposition.resid.plot(ax=axes[3], color='#95a5a6')
    axes[3].set_ylabel('Resíduo', fontsize=12)
    axes[3].set_xlabel('Ano', fontsize=12)
    axes[3].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/decomposition_japan.png', dpi=300, bbox_inches='tight')
    
    print("Análise de Decomposição - Japão")
    print("=" * 50)
    print("\nA série possui Tendência? Sim, tendência não linear")
    print("Tipo: Crescente de 1950 até ~1998 (pico ~31.000), depois decrescente até 2020")
    print("\nA série possui Sazonalidade? Sim")
    print("Período: Aproximadamente 12-15 anos (ciclos regulares visíveis)")
    print("\nA série apresenta um Ciclo? Sim")
    print("Razão: Possíveis fatores socioeconômicos, crises econômicas,")
    print("       mudanças culturais e políticas de saúde mental no Japão")
    print("\nGráfico salvo em: graphs/decomposition_japan.png")


if __name__ == "__main__":
    analyze_japan_decomposition()
