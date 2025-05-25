import plotly.graph_objects as go
import os

# Data for each table
tables = {
    "Bengali": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4227, 2.6649, 1.9364, 1.7350, 2.6117, 1.0824, 3.2488, 2.6603],
        "mcd": [733.9330, 224.3300, 217.1180, 229.1400, 125.6720, 830.5780, 111.0770, 188.8110],
        "msd": [0.0037, 0.0036, 0.0036, 0.0035, 0.0031, 0.0019, 0.0034, 0.0037],
        "stoi": [0.1138, 0.9443, 0.8961, 0.8846, 0.9444, 0.3452, 0.9730, 0.9466],
        "pcc": [-0.0003, -0.0431, -0.0028, -0.0029, 0.0017, 0.0002, 0.0071, -0.0307]
    },
    "Bhojpuri": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4046, 2.8399, 2.1152, 1.9042, 2.7969, 1.0674, 3.4829, 2.9347],
        "mcd": [713.6930, 213.6170, 204.3160, 225.3850, 132.1360, 826.4380, 116.2160, 196.0160],
        "msd": [0.0037, 0.0035, 0.0036, 0.0035, 0.0031, 0.0019, 0.0035, 0.0036],
        "stoi": [0.1119, 0.9574, 0.9135, 0.8989, 0.9399, 0.5375, 0.9779, 0.9585],
        "pcc": [0.0005, -0.0104, 0.0048, -0.0010, -0.0072, 0.0087, 0.0231, -0.0101]
    },
    "Chhattisgarhi": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4618, 2.8622, 2.1243, 1.8805, 2.6591, 1.0723, 3.3068, 2.8130],
        "mcd": [745.0920, 201.3560, 202.8900, 218.8400, 122.3650, 839.4440, 111.0880, 184.9960],
        "msd": [0.0041, 0.0040, 0.0040, 0.0040, 0.0033, 0.0021, 0.0039, 0.0040],
        "stoi": [0.0970, 0.9609, 0.9145, 0.9047, 0.9452, 0.3617, 0.9765, 0.9573],
        "pcc": [0.0005, -0.0256, 0.0058, -0.0053, 0.0113, 0.0003, -0.0033, -0.0102]
    },
    "Gujarati": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4227, 2.1620, 1.9558, 1.7638, 2.5013, 1.1012, 3.2878, 2.7592],
        "mcd": [722.9470, 234.9950, 223.5710, 242.6300, 117.8530, 816.8120, 84.5728, 154.9000],
        "msd": [0.0033, 0.0026, 0.0028, 0.0027, 0.0026, 0.0017, 0.0033, 0.0027],
        "stoi": [0.0903, 0.8826, 0.8687, 0.8423, 0.9235, 0.4087, 0.9691, 0.9466],
        "pcc": [-0.0025, 0.0135, -0.0020, -0.0104, -0.0078, 0.0010, -0.0522, 0.1021]
    },
    "Hindi": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4645, 2.3623, 1.7673, 1.6082, 2.4880, 1.1061, 3.3172, 2.8347],
        "mcd": [815.7700, 253.2100, 244.6770, 267.1760, 126.5080, 847.5010, 105.6720, 168.7680],
        "msd": [0.0060, 0.0054, 0.0052, 0.0051, 0.0051, 0.0031, 0.0053, 0.0060],
        "stoi": [0.1085, 0.9307, 0.8848, 0.8662, 0.9503, 0.3875, 0.9812, 0.9616],
        "pcc": [0.0008, -0.0689, 0.0072, -0.0096, -0.0153, -0.0022, 0.0858, -0.0594]
    },
    "Kannada": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4843, 2.4813, 1.9486, 1.7356, 2.5898, 1.0763, 3.3003, 2.8699],
        "mcd": [865.5120, 267.8480, 268.9600, 296.1000, 151.6560, 919.5720, 128.1810, 208.1550],
        "msd": [0.0032, 0.0030, 0.0029, 0.0030, 0.0026, 0.0016, 0.0028, 0.0033],
        "stoi": [0.1101, 0.9416, 0.8962, 0.8785, 0.9459, 0.4186, 0.9797, 0.9599],
        "pcc": [0.0000, -0.0456, 0.0099, -0.0134, 0.0072, 0.0013, 0.0486, -0.0573]
    },
    "Magahi": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4323, 2.8599, 2.1466, 1.8922, 2.7258, 1.0834, 3.4503, 2.9764],
        "mcd": [675.8480, 193.3590, 185.3740, 209.6610, 120.9320, 794.3330, 102.4990, 171.4780],
        "msd": [0.0052, 0.0048, 0.0049, 0.0049, 0.0043, 0.0027, 0.0049, 0.0050],
        "stoi": [0.1028, 0.9550, 0.9166, 0.9043, 0.9439, 0.3415, 0.9779, 0.9616],
        "pcc": [-0.0004, -0.0168, 0.0047, -0.0153, -0.0107, -0.0032, 0.0156, -0.0253]
    },
    "Maithili": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4459, 2.6738, 1.9439, 1.7781, 2.5654, 1.0598, 3.2350, 2.6369],
        "mcd": [618.5620, 208.4410, 206.3880, 219.7220, 112.1820, 701.5180, 98.8438, 170.3070],
        "msd": [0.0029, 0.0028, 0.0029, 0.0029, 0.0024, 0.0015, 0.0026, 0.0029],
        "stoi": [0.1196, 0.9465, 0.8931, 0.8855, 0.9416, 0.5437, 0.9730, 0.9462],
        "pcc": [0.0008, -0.0162, 0.0022, -0.0110, -0.0052, 0.0100, 0.0534, -0.0517]
    },
    "Marathi": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.5123, 2.5342, 1.9732, 1.8042, 2.6678, 1.0719, 3.3501, 2.8057],
        "mcd": [771.1270, 247.0370, 252.7560, 266.6000, 130.9850, 816.8120, 122.7180, 199.6530],
        "msd": [0.0021, 0.0020, 0.0022, 0.0021, 0.0018, 0.0010, 0.0019, 0.0022],
        "stoi": [0.1193, 0.9370, 0.8924, 0.8761, 0.9392, 0.5813, 0.9776, 0.9566],
        "pcc": [0.0000, -0.0198, -0.0099, 0.0026, -0.0014, -0.0094, 0.0500, -0.0537]
    },
    "Telugu": {
        "vocoders": ["BigVGAN", "DiffWave", "Multi-band MelGAN (1)", "Multi-band MelGAN (2)", "HiFi-GAN", "Parallel WaveGAN", "UniVNet", "VocGAN"],
        "pesq": [4.4884, 2.8155, 2.0267, 1.8297, 2.6801, 1.0829, 3.4107, 2.9835],
        "mcd": [765.4330, 211.6840, 215.2930, 230.0980, 122.3530, 855.6690, 128.6440, 176.2040],
        "msd": [0.0044, 0.0044, 0.0042, 0.0041, 0.0037, 0.0022, 0.0041, 0.0043],
        "stoi": [0.1249, 0.9579, 0.9094, 0.8959, 0.9473, 0.5966, 0.9802, 0.9640],
        "pcc": [-0.0027, -0.0419, 0.0080, 0.0013, 0.0027, -0.0057, 0.0201, -0.0162]
    }
}

# Create a single HTML file with all plots
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Vocoder Performance Comparison</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
"""

for language, data in tables.items():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data["vocoders"], y=data["pesq"], name='PESQ', marker_color='rgb(55, 83, 109)'))
    fig.add_trace(go.Bar(x=data["vocoders"], y=data["mcd"], name='MCD', marker_color='rgb(26, 118, 255)'))
    fig.add_trace(go.Bar(x=data["vocoders"], y=data["msd"], name='MSD', marker_color='rgb(255, 144, 14)'))
    fig.add_trace(go.Bar(x=data["vocoders"], y=data["stoi"], name='STOI', marker_color='rgb(44, 160, 101)'))
    fig.add_trace(go.Bar(x=data["vocoders"], y=data["pcc"], name='PCC', marker_color='rgb(255, 65, 54)'))

    fig.update_layout(
        title=f'Performance Comparison of Vocoders Across Metrics for {language}',
        xaxis_title='Vocoder',
        yaxis_title='Score',
        barmode='group',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    html_content += fig.to_html(full_html=False)

html_content += """
</body>
</html>
"""

# Save the combined HTML content to a file
with open("vocoder_performance_comparison.html", "w") as file:
    file.write(html_content)

# Open the HTML file in a web browser
import webbrowser
webbrowser.open('file://' + os.path.realpath("vocoder_performance_comparison.html"))

