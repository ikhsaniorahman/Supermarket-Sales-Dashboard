import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app


layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1(
                    "Hypothesis Testing",
                    className="text-center",
                ),
                className="mb-4 mt-5"
            )
        ),
    ]),

    dbc.Container([

        dbc.Row([
            dbc.Col([
                dcc.Markdown([
                    '''
                        ## Dataset

                        Dataset merupakan data history penjualan supermarket di 3 cabang berbeda selama 3 bulan pada tahun 2019.

                    '''
                ], className="mb-5")
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Markdown([
                    '''
                        ## Objective

                        Objective hyphotestis testing adalah melakukan uji statistik terhadap dataset untuk melihat apakah ada kemungkinan 
                        hubungan antara jumlah total sales pelanggan yang telah menjadi Member dengan pelanggan non-Member.

                    '''
                ], className="mb-5")
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Markdown([
                    '''
                        ## Metode

                        Metode hyphotesis yang digunakan adalah Two-tailed test.

                    '''
                ], className="mb-5")
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Markdown([
                    '''
                        ## Hypothesis

                        
                        - Hypothesis Null (H0) = tidak ada perbedaan rata-rata total sales pelanggan Member dengan pelanggan non-Member.
                        - Hypothesis alternatif (H1) = ada perbedaan rata-rata total sales pelanggan Member dengan pelanggan non-Member.

                        '''
                ]),
                html.Img(src=app.get_asset_url(
                    'mean_cust.PNG'), className="mb-5"),
            ]),
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Markdown([
                    '''
                        ## Kriteria Hyphotesis Testing

                        Berikut adalah kriteria diterima atau tidaknya sebuah hypothesis:
                        
                        α = 0,05

                        - Hypothesis Null(H0) diterima jika hasil uji (p-value) **lebih besar** dari α.
                        - Hypothesis alternatif(H1) diterima jika hasil uji (p-value) **lebih kecil** dari α.

                        '''
                ], className="mb-5")
            ])
        ]),

        dbc.Row([
                dbc.Col([
                    dcc.Markdown(
                        '''
                        ## Hasil Hyphotesis Testing
                        Hasil menunjukkan bahwa p-value senilai 0.566
                        '''
                    ),
                    html.Img(src=app.get_asset_url(
                        'hasil_pvalue.PNG'), className="mb-5"),
                ]),
                ]),

        dbc.Row([
                dbc.Col([
                    dcc.Markdown(
                        '''
                        ## Kesimpulan

                        Dari hasil hypothesis testing diperoleh hasil dan kesimpulan sebagai berikut:

                        - Hypothesis Null(H0) gagal di-reject, karena p-value senilai 0.566 lebih besar dari α (0,05)
                        - Hypothesis Null(H0) gagal di-reject, sehingga dapat disimpulkan bahwa kita kekurangan bukti untuk dapat menolak H0 agar dapat menerima pernyataan H1.

                        '''
                    )
                ])
                ]),

    ])
])
