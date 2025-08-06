import numpy as np
import matplotlib.pyplot as plt

# Simulate BAO correlation function ξ(r) for isotropic and anisotropic cases
r_bao = np.linspace(50, 200, 500)  # separation in Mpc/h

# Baseline ΛCDM-like BAO signal
bao_peak_pos = 105  # Mpc/h
xi_LCDM = 0.01 * np.exp(-(r_bao - bao_peak_pos)**2 / (2 * 8**2)) * np.cos((r_bao - bao_peak_pos)/10)
xi_LCDM += 0.002 * np.exp(-r_bao/50)  # background damping

# FDFT modification: amplitude enhancement
xi_FDFT_iso = 1.05 * xi_LCDM

# FDFT anisotropic modification: small peak shift Δr_s/r_s ~ 10⁻³
delta_r = bao_peak_pos * 1e-3
xi_FDFT_aniso = 1.05 * np.exp(-(r_bao - (bao_peak_pos + delta_r))**2 / (2 * 8**2)) \
                * np.cos((r_bao - (bao_peak_pos + delta_r))/10)
xi_FDFT_aniso += 0.002 * np.exp(-r_bao/50)

# Dark background style
plt.style.use("dark_background")
plt.rcParams.update({
    "figure.dpi": 160,
    "savefig.dpi": 300,
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "legend.fontsize": 11,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "axes.linewidth": 1.0,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "mathtext.fontset": "stix",
    "font.family": "STIXGeneral",
})

fig, ax = plt.subplots(figsize=(9.5, 6.5))

# Plot BAO signals
ax.plot(r_bao, xi_LCDM, color="#ff6b6b", lw=2.0, label=r"$\Lambda$CDM")
ax.plot(r_bao, xi_FDFT_iso, color="#4dabf7", lw=2.5, label="FDFT (isotropic)")
ax.plot(r_bao, xi_FDFT_aniso, color="#82c91e", lw=2.2, ls="--", label="FDFT (anisotropic)")

# Mark BAO peak
ax.axvline(bao_peak_pos, color="white", lw=1.2, ls="--", alpha=0.5)
ax.text(bao_peak_pos, 0.0085, "BAO peak", ha="center", va="bottom", fontsize=10, color="white")

# Labels and limits
ax.set_title("Baryon Acoustic Oscillations (BAO): Isotropic vs Anisotropic FDFT", pad=12)
ax.set_xlabel(r"Separation $r$ [Mpc/$h$]")
ax.set_ylabel(r"Correlation function $\xi(r)$")
ax.set_xlim(50, 200)
ax.set_ylim(-0.002, 0.012)
ax.grid(True, which="both", alpha=0.3)
ax.minorticks_on()
ax.tick_params(axis="both", which="both", direction="in", top=True, right=True)

# Legend
ax.legend(frameon=False, loc="upper right")

# Save
out_path = "section4_fdft_BAO_anisotropy_dark.png"
plt.tight_layout()
plt.savefig(out_path, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.show()
