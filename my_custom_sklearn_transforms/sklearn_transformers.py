{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Aula_2_Pandas.ipynb",
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOUNFHj0Dq4wVnyGSIN+Gnf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ClarisseAlvarenga/btc_ibm_desafio_cocamar/blob/master/Aula_2_Pandas.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gcmqU26nk0tX",
        "colab_type": "text"
      },
      "source": [
        "# PANDAS BÁSICO"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KWNJAV22lJK9",
        "colab_type": "text"
      },
      "source": [
        "## IMPORTANDO AS BIBLIOTECAS"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bq7Rm_g7kpqf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "db4dc140-4936-4d9a-d13c-4b09ad238413"
      },
      "source": [
        "#importando as bibliotecas\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from statsmodels.stats.weightstats import DescrStatsW\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.\n",
            "  import pandas.util.testing as tm\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pdrVK_xQmRO6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#lendo o arquivo\n",
        "dados = pd.read_csv('/content/dataset_desafio_2.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F_3ijyfYnpA1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "outputId": "f867fdcd-8d2e-4f5b-c696-d011e4d61659"
      },
      "source": [
        "#visualizar\n",
        "dados.head(1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MATRICULA</th>\n",
              "      <th>NOME</th>\n",
              "      <th>REPROVACOES_DE</th>\n",
              "      <th>REPROVACOES_EM</th>\n",
              "      <th>REPROVACOES_MF</th>\n",
              "      <th>REPROVACOES_GO</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_GO</th>\n",
              "      <th>INGLES</th>\n",
              "      <th>H_AULA_PRES</th>\n",
              "      <th>TAREFAS_ONLINE</th>\n",
              "      <th>FALTAS</th>\n",
              "      <th>PERFIL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>502375</td>\n",
              "      <td>Márcia Illiglener</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6.2</td>\n",
              "      <td>5.8</td>\n",
              "      <td>4.6</td>\n",
              "      <td>5.9</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>EXATAS</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   MATRICULA               NOME  REPROVACOES_DE  ...  TAREFAS_ONLINE  FALTAS  PERFIL\n",
              "0     502375  Márcia Illiglener               0  ...               4       3  EXATAS\n",
              "\n",
              "[1 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QMwLzvKiJobe",
        "colab_type": "text"
      },
      "source": [
        "## SEPARAR OS DATASETS"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oYSa4p76JsMU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "24bbb09b-d7cc-4446-c683-74d2da04977a"
      },
      "source": [
        "dados.PERFIL.unique()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['EXATAS', 'HUMANAS', 'DIFICULDADE', 'MUITO_BOM', 'EXCELENTE'],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lNmVJ_uxJ6CN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#separando os datasets\n",
        "dificuldade = dados.loc[dados['PERFIL'] == 'DIFICULDADE' ]\n",
        "exatas = dados.query('PERFIL == \"EXATAS\"')\n",
        "humanas = dados.loc[dados['PERFIL'] == 'HUMANAS']\n",
        "muito_bom = dados.query('PERFIL == \"MUITO_BOM\"')\n",
        "excelente = dados.loc[dados['PERFIL'] == 'EXCELENTE']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1CllajuqKIAD",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 111
        },
        "outputId": "cbf192c9-ff17-4cfb-8744-3c0b53a1c8ba"
      },
      "source": [
        "dificuldade.head(2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MATRICULA</th>\n",
              "      <th>NOME</th>\n",
              "      <th>REPROVACOES_DE</th>\n",
              "      <th>REPROVACOES_EM</th>\n",
              "      <th>REPROVACOES_MF</th>\n",
              "      <th>REPROVACOES_GO</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_GO</th>\n",
              "      <th>INGLES</th>\n",
              "      <th>H_AULA_PRES</th>\n",
              "      <th>TAREFAS_ONLINE</th>\n",
              "      <th>FALTAS</th>\n",
              "      <th>PERFIL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>192652</td>\n",
              "      <td>Fernanda Guedes</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>DIFICULDADE</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>949491</td>\n",
              "      <td>Alessandre Borba Gomes</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5</td>\n",
              "      <td>2</td>\n",
              "      <td>5</td>\n",
              "      <td>DIFICULDADE</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   MATRICULA                    NOME  ...  FALTAS       PERFIL\n",
              "3     192652         Fernanda Guedes  ...       4  DIFICULDADE\n",
              "4     949491  Alessandre Borba Gomes  ...       5  DIFICULDADE\n",
              "\n",
              "[2 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TpPAmNFIKKCj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 111
        },
        "outputId": "390743f0-4833-4daf-c6d9-d8cee1c0ded1"
      },
      "source": [
        "exatas.head(2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MATRICULA</th>\n",
              "      <th>NOME</th>\n",
              "      <th>REPROVACOES_DE</th>\n",
              "      <th>REPROVACOES_EM</th>\n",
              "      <th>REPROVACOES_MF</th>\n",
              "      <th>REPROVACOES_GO</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_GO</th>\n",
              "      <th>INGLES</th>\n",
              "      <th>H_AULA_PRES</th>\n",
              "      <th>TAREFAS_ONLINE</th>\n",
              "      <th>FALTAS</th>\n",
              "      <th>PERFIL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>502375</td>\n",
              "      <td>Márcia Illiglener</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6.2</td>\n",
              "      <td>5.8</td>\n",
              "      <td>4.6</td>\n",
              "      <td>5.9</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>EXATAS</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>397093</td>\n",
              "      <td>Jason Jytereoman Izoimum</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>6.2</td>\n",
              "      <td>5.2</td>\n",
              "      <td>4.5</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>EXATAS</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   MATRICULA                      NOME  ...  FALTAS  PERFIL\n",
              "0     502375         Márcia Illiglener  ...       3  EXATAS\n",
              "1     397093  Jason Jytereoman Izoimum  ...       3  EXATAS\n",
              "\n",
              "[2 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z_o-EJ5RLLMr",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 111
        },
        "outputId": "7401b4dc-73c3-4ad5-ee64-a72e21c9e191"
      },
      "source": [
        "humanas.head(2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MATRICULA</th>\n",
              "      <th>NOME</th>\n",
              "      <th>REPROVACOES_DE</th>\n",
              "      <th>REPROVACOES_EM</th>\n",
              "      <th>REPROVACOES_MF</th>\n",
              "      <th>REPROVACOES_GO</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_GO</th>\n",
              "      <th>INGLES</th>\n",
              "      <th>H_AULA_PRES</th>\n",
              "      <th>TAREFAS_ONLINE</th>\n",
              "      <th>FALTAS</th>\n",
              "      <th>PERFIL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>915288</td>\n",
              "      <td>Bartolomeu Inácio da Gama</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>7.3</td>\n",
              "      <td>6.7</td>\n",
              "      <td>7.1</td>\n",
              "      <td>7.2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>HUMANAS</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>627360</td>\n",
              "      <td>Magali Hellen Gejibaflião</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>7.3</td>\n",
              "      <td>7.4</td>\n",
              "      <td>7.6</td>\n",
              "      <td>6.5</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5</td>\n",
              "      <td>3</td>\n",
              "      <td>5</td>\n",
              "      <td>HUMANAS</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   MATRICULA                       NOME  ...  FALTAS   PERFIL\n",
              "2     915288  Bartolomeu Inácio da Gama  ...       3  HUMANAS\n",
              "5     627360  Magali Hellen Gejibaflião  ...       5  HUMANAS\n",
              "\n",
              "[2 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_5x7aPFTLM_x",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 145
        },
        "outputId": "376b2fae-a236-465a-a660-2c6e3ed4566b"
      },
      "source": [
        "muito_bom.head(2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MATRICULA</th>\n",
              "      <th>NOME</th>\n",
              "      <th>REPROVACOES_DE</th>\n",
              "      <th>REPROVACOES_EM</th>\n",
              "      <th>REPROVACOES_MF</th>\n",
              "      <th>REPROVACOES_GO</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_GO</th>\n",
              "      <th>INGLES</th>\n",
              "      <th>H_AULA_PRES</th>\n",
              "      <th>TAREFAS_ONLINE</th>\n",
              "      <th>FALTAS</th>\n",
              "      <th>PERFIL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>382592</td>\n",
              "      <td>Matheus de Souza dos Pinhais</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6.9</td>\n",
              "      <td>7.5</td>\n",
              "      <td>7.3</td>\n",
              "      <td>6.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>5</td>\n",
              "      <td>5</td>\n",
              "      <td>MUITO_BOM</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28</th>\n",
              "      <td>194445</td>\n",
              "      <td>Aécio Eric de Freitas Júnior</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6.7</td>\n",
              "      <td>7.0</td>\n",
              "      <td>5.9</td>\n",
              "      <td>5.6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>MUITO_BOM</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    MATRICULA                          NOME  ...  FALTAS     PERFIL\n",
              "10     382592  Matheus de Souza dos Pinhais  ...       5  MUITO_BOM\n",
              "28     194445  Aécio Eric de Freitas Júnior  ...       4  MUITO_BOM\n",
              "\n",
              "[2 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ah96Nj0JLWta",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 128
        },
        "outputId": "d208c71c-35ca-41fb-f054-dd5c18f9f556"
      },
      "source": [
        "excelente.head(2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MATRICULA</th>\n",
              "      <th>NOME</th>\n",
              "      <th>REPROVACOES_DE</th>\n",
              "      <th>REPROVACOES_EM</th>\n",
              "      <th>REPROVACOES_MF</th>\n",
              "      <th>REPROVACOES_GO</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_GO</th>\n",
              "      <th>INGLES</th>\n",
              "      <th>H_AULA_PRES</th>\n",
              "      <th>TAREFAS_ONLINE</th>\n",
              "      <th>FALTAS</th>\n",
              "      <th>PERFIL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>506004</td>\n",
              "      <td>Sâmia Edilene Sayu de Meireles</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>8.0</td>\n",
              "      <td>8.4</td>\n",
              "      <td>10.0</td>\n",
              "      <td>8.5</td>\n",
              "      <td>0.0</td>\n",
              "      <td>10</td>\n",
              "      <td>6</td>\n",
              "      <td>2</td>\n",
              "      <td>EXCELENTE</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>104</th>\n",
              "      <td>527716</td>\n",
              "      <td>Priscila de Drummond</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>7.9</td>\n",
              "      <td>7.2</td>\n",
              "      <td>9.4</td>\n",
              "      <td>7.9</td>\n",
              "      <td>1.0</td>\n",
              "      <td>12</td>\n",
              "      <td>5</td>\n",
              "      <td>4</td>\n",
              "      <td>EXCELENTE</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     MATRICULA                            NOME  ...  FALTAS     PERFIL\n",
              "22      506004  Sâmia Edilene Sayu de Meireles  ...       2  EXCELENTE\n",
              "104     527716            Priscila de Drummond  ...       4  EXCELENTE\n",
              "\n",
              "[2 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7Z4J4KmCLcGZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "mf_humanas = DescrStatsW(humanas['INGLES'].dropna())\n",
        "mf_exatas = DescrStatsW(exatas['INGLES'].dropna())"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HVmvFsiUMyRF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "comparacao1 = mf_humanas.get_compare(mf_exatas)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bP4K4QlPNQ5N",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        },
        "outputId": "d6dc9cac-b6e0-48db-aab3-83450841dfc9"
      },
      "source": [
        "print(comparacao1.summary())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "                          Test for equality of means                          \n",
            "==============================================================================\n",
            "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
            "------------------------------------------------------------------------------\n",
            "subset #1     -0.0927      0.011     -8.396      0.000      -0.114      -0.071\n",
            "==============================================================================\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3fMqfvYjNW8-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4h0yfVshO9eU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 406
        },
        "outputId": "dafc5c43-4cf9-4f1a-9a96-4c0aad8572c1"
      },
      "source": [
        "plt.figure(figsize=(12,6))\n",
        "sns.boxplot(excelente['NOTA_MF'])\n",
        "#sns.boxplot(muito_bom['NOTA_MF'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f986c850d68>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2g0HrBpHPGOD",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 498
        },
        "outputId": "c1c4b31d-e460-4306-e058-279837182576"
      },
      "source": [
        "plt.figure(figsize=(15,8))\n",
        "sns.boxplot(y=dados['NOTA_DE'], x=dados['PERFIL']);"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xWxxiqhmTIYM",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 499
        },
        "outputId": "1aeb9750-1560-448e-e5d2-26dd5a78c2c7"
      },
      "source": [
        "plt.figure(figsize=(15,8))\n",
        "sns.boxplot(y=dados['NOTA_MF'], x=dados['PERFIL']);"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bi_dqEegTf3x",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 498
        },
        "outputId": "bba6b34e-926d-4d2d-9ffd-f568907f830e"
      },
      "source": [
        "plt.figure(figsize=(15,8))\n",
        "sns.boxplot(y=dados['NOTA_GO'], x=dados['PERFIL']);"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1Rz38RPQTyvJ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "c5b27409-2dbd-4a50-ce5e-7fca459d17c2"
      },
      "source": [
        "humanas[['NOTA_MF', 'NOTA_EM', 'NOTA_DE', 'NOTA_GO']].describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_GO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>3196.000000</td>\n",
              "      <td>3196.000000</td>\n",
              "      <td>3196.000000</td>\n",
              "      <td>2634.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>7.366458</td>\n",
              "      <td>6.619931</td>\n",
              "      <td>6.708448</td>\n",
              "      <td>6.145976</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.628754</td>\n",
              "      <td>0.800094</td>\n",
              "      <td>0.611674</td>\n",
              "      <td>0.814659</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>6.600000</td>\n",
              "      <td>3.900000</td>\n",
              "      <td>4.200000</td>\n",
              "      <td>4.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>6.900000</td>\n",
              "      <td>6.100000</td>\n",
              "      <td>6.400000</td>\n",
              "      <td>5.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>7.200000</td>\n",
              "      <td>6.700000</td>\n",
              "      <td>6.800000</td>\n",
              "      <td>6.200000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>7.700000</td>\n",
              "      <td>7.200000</td>\n",
              "      <td>7.100000</td>\n",
              "      <td>6.800000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>10.700000</td>\n",
              "      <td>9.000000</td>\n",
              "      <td>8.400000</td>\n",
              "      <td>9.600000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "           NOTA_MF      NOTA_EM      NOTA_DE      NOTA_GO\n",
              "count  3196.000000  3196.000000  3196.000000  2634.000000\n",
              "mean      7.366458     6.619931     6.708448     6.145976\n",
              "std       0.628754     0.800094     0.611674     0.814659\n",
              "min       6.600000     3.900000     4.200000     4.100000\n",
              "25%       6.900000     6.100000     6.400000     5.600000\n",
              "50%       7.200000     6.700000     6.800000     6.200000\n",
              "75%       7.700000     7.200000     7.100000     6.800000\n",
              "max      10.700000     9.000000     8.400000     9.600000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KewDDv6xUAy5",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "3227cf92-66bb-447f-8879-dcdf22a29117"
      },
      "source": [
        "exatas[['NOTA_MF', 'NOTA_EM', 'NOTA_DE', 'NOTA_GO']].describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_GO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>8230.000000</td>\n",
              "      <td>8230.000000</td>\n",
              "      <td>8230.000000</td>\n",
              "      <td>6652.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5.515346</td>\n",
              "      <td>6.066379</td>\n",
              "      <td>6.254921</td>\n",
              "      <td>5.545941</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.748003</td>\n",
              "      <td>0.780667</td>\n",
              "      <td>0.629921</td>\n",
              "      <td>0.867095</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>5.100000</td>\n",
              "      <td>5.500000</td>\n",
              "      <td>5.900000</td>\n",
              "      <td>5.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>5.600000</td>\n",
              "      <td>6.100000</td>\n",
              "      <td>6.300000</td>\n",
              "      <td>5.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>6.000000</td>\n",
              "      <td>6.700000</td>\n",
              "      <td>6.700000</td>\n",
              "      <td>6.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>6.600000</td>\n",
              "      <td>8.500000</td>\n",
              "      <td>8.300000</td>\n",
              "      <td>7.900000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "           NOTA_MF      NOTA_EM      NOTA_DE      NOTA_GO\n",
              "count  8230.000000  8230.000000  8230.000000  6652.000000\n",
              "mean      5.515346     6.066379     6.254921     5.545941\n",
              "std       0.748003     0.780667     0.629921     0.867095\n",
              "min       0.000000     0.000000     0.000000     0.000000\n",
              "25%       5.100000     5.500000     5.900000     5.100000\n",
              "50%       5.600000     6.100000     6.300000     5.500000\n",
              "75%       6.000000     6.700000     6.700000     6.100000\n",
              "max       6.600000     8.500000     8.300000     7.900000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cQXdWcKyUrSY",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "8fec5cf1-5e9d-4c50-e58f-540a48b5e1fc"
      },
      "source": [
        "excelente[['NOTA_MF', 'NOTA_EM', 'NOTA_DE', 'NOTA_GO']].describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_GO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>671.000000</td>\n",
              "      <td>671.000000</td>\n",
              "      <td>671.000000</td>\n",
              "      <td>544.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>8.663785</td>\n",
              "      <td>7.889270</td>\n",
              "      <td>7.570045</td>\n",
              "      <td>7.462316</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>1.033419</td>\n",
              "      <td>0.500422</td>\n",
              "      <td>0.418076</td>\n",
              "      <td>0.594229</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>5.200000</td>\n",
              "      <td>6.200000</td>\n",
              "      <td>5.100000</td>\n",
              "      <td>5.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>8.100000</td>\n",
              "      <td>7.500000</td>\n",
              "      <td>7.300000</td>\n",
              "      <td>7.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>8.700000</td>\n",
              "      <td>7.900000</td>\n",
              "      <td>7.600000</td>\n",
              "      <td>7.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>9.300000</td>\n",
              "      <td>8.200000</td>\n",
              "      <td>7.800000</td>\n",
              "      <td>7.825000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>11.500000</td>\n",
              "      <td>9.400000</td>\n",
              "      <td>9.000000</td>\n",
              "      <td>10.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          NOTA_MF     NOTA_EM     NOTA_DE     NOTA_GO\n",
              "count  671.000000  671.000000  671.000000  544.000000\n",
              "mean     8.663785    7.889270    7.570045    7.462316\n",
              "std      1.033419    0.500422    0.418076    0.594229\n",
              "min      5.200000    6.200000    5.100000    5.500000\n",
              "25%      8.100000    7.500000    7.300000    7.100000\n",
              "50%      8.700000    7.900000    7.600000    7.500000\n",
              "75%      9.300000    8.200000    7.800000    7.825000\n",
              "max     11.500000    9.400000    9.000000   10.000000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YnnL24LLVRzI",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "4d2c7c15-ef61-4c33-ef94-6828eadfb412"
      },
      "source": [
        "dificuldade[['NOTA_MF', 'NOTA_EM', 'NOTA_DE', 'NOTA_GO']].describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>NOTA_MF</th>\n",
              "      <th>NOTA_EM</th>\n",
              "      <th>NOTA_DE</th>\n",
              "      <th>NOTA_GO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>7001.000000</td>\n",
              "      <td>7001.000000</td>\n",
              "      <td>7001.000000</td>\n",
              "      <td>5714.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2.129624</td>\n",
              "      <td>2.668833</td>\n",
              "      <td>2.789916</td>\n",
              "      <td>2.041267</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>2.686717</td>\n",
              "      <td>2.776931</td>\n",
              "      <td>2.886827</td>\n",
              "      <td>2.566527</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>5.100000</td>\n",
              "      <td>5.400000</td>\n",
              "      <td>5.700000</td>\n",
              "      <td>4.900000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>8.900000</td>\n",
              "      <td>8.500000</td>\n",
              "      <td>7.900000</td>\n",
              "      <td>7.800000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "           NOTA_MF      NOTA_EM      NOTA_DE      NOTA_GO\n",
              "count  7001.000000  7001.000000  7001.000000  5714.000000\n",
              "mean      2.129624     2.668833     2.789916     2.041267\n",
              "std       2.686717     2.776931     2.886827     2.566527\n",
              "min       0.000000     0.000000     0.000000     0.000000\n",
              "25%       0.000000     0.000000     0.000000     0.000000\n",
              "50%       0.000000     0.000000     0.000000     0.000000\n",
              "75%       5.100000     5.400000     5.700000     4.900000\n",
              "max       8.900000     8.500000     7.900000     7.800000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4N3u_UhuVtme",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 289
        },
        "outputId": "b5076862-d6dc-45f1-e0aa-d485b894e51b"
      },
      "source": [
        "dados.isna().sum()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "MATRICULA            0\n",
              "NOME                 0\n",
              "REPROVACOES_DE       0\n",
              "REPROVACOES_EM       0\n",
              "REPROVACOES_MF       0\n",
              "REPROVACOES_GO       0\n",
              "NOTA_DE              0\n",
              "NOTA_EM              0\n",
              "NOTA_MF              0\n",
              "NOTA_GO           3716\n",
              "INGLES            3628\n",
              "H_AULA_PRES          0\n",
              "TAREFAS_ONLINE       0\n",
              "FALTAS               0\n",
              "PERFIL               0\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "h4_1gNlYWmGM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
