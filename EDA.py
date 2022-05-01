import neurokit2 as nk
import matplotlib.pyplot as plt
%matplotlib online
plt.rcParams['figure.figsize'] = [15, 5]
# Simulate 10 seconds of EDA Signal (recorded at 250 samples / second)
eda_signal = nk.eda_simulate(duration=10, sampling_rate=250, scr_number=3, drift=0.01)
# Process the raw EDA signal
 signals, info = nk.eda_process(eda_signal, sampling_rate=250)
# Extract clean EDA and SCR features
cleaned = signals["EDA_Clean"]
features = [info["SCR_Onsets"], info["SCR_Peaks"], info["SCR_Recovery"]]
# Visualize SCR features in cleaned EDA signal
plot = nk.events_plot(features, cleaned, color=['red', 'blue', 'orange'])
# Filter phasic and tonic components
data = nk.eda_phasic(nk.standardize(eda_signal), sampling_rate=250)
data["EDA_Raw"] = eda_signal  # Add raw signal
data.plot()
# Plot EDA signal
plot = nk.eda_plot(signals)
