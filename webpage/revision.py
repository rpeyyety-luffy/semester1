# One-page quick revision sheet for each unit (Markdown).
# Built from the key points in the Q&A answers: definitions, formulas, flows, one-liners.

REVISION = {
    "Unit 1": """
### 🔑 Key definitions
| Term | One-line meaning |
|---|---|
| Communication | Transferring information from a source to a destination through a channel |
| 5 elements | Sender, message, medium/channel, receiver, agreed method of interpretation |
| Computer network | Interconnected devices that exchange information and share resources |
| Internetworking | Linking different networks (via routers) so data crosses network boundaries |
| Internet | Global network of networks using the TCP/IP suite — not centrally owned |
| Protocol | Rules: message format, order, sender identity, error handling |
| IoP vs IoT | IoP connects people (email, social media); IoT connects sensors, machines, vehicles |
| Sensor | Converts a physical quantity into an electrical / digital signal |
| Controller | Reads sensor output, applies logic (e.g. ESP32, PLC) |
| Actuator | Produces a physical effect after a command (relay, pump, valve, light) |
| Cloud | Remote storage + computation: history, patterns, graphs, notifications |

### 🔁 Flows to remember
- **IoT chain:** Sensor → Controller → Connectivity (Wi-Fi/Bluetooth) → Router → ISP → Cloud → User / Action
- **Closed loop:** Sensor measures → Controller compares with threshold → Actuator acts → Sensor measures the result again
- **Smart irrigation:** Soil-moisture sensor → ESP32 → Relay → Pump/valve (stop when moisture is enough)
- **Smartwatch:** Heart-rate sensor → Bluetooth → Phone → Wi-Fi/cellular → Cloud → Notification
- **History:** Messengers/letters → Telegraph → Telephone → Radio → TV → Digital (bits over networks)

### 🎯 Sensor picks
| Application | Sensor |
|---|---|
| Smartwatch | Heart-rate |
| Streetlight | Light (optical) + motion |
| Irrigation | Soil moisture |
| Factory machine | Industrial temperature |

### 💬 One-liners for Evaluate answers
- "The sensor observes, the controller decides and the actuator acts."
- Cloud = history and large-scale analysis; **edge/local** = immediate action.
- Closed loop beats display-only: automatic, fast, 24×7, less human effort.
- IoT concerns: cloud/Internet dependence, privacy, cybersecurity.
""",
    "Unit 2": """
### 🧮 Formulas
| Quantity | Formula | Unit |
|---|---|---|
| Ohm's law | **V = I × R** | V, A, Ω |
| Power | **P = V × I** = I²R = V²/R | Watt (W) |
| Energy | **E = P × t** | kWh (1 unit = 1 kWh) |
| EMF vs terminal voltage | EMF = V + internal drop | V |

**Worked:** 12 V, 6 Ω → **2 A** · 230 V, 5 A → **1150 W** · 100 W × 5 h → **0.5 kWh**

### 🔌 Circuit elements
| Element | Energy | Felt when | Unit |
|---|---|---|---|
| Resistor | Dissipates as heat | Always | Ohm (Ω) |
| Inductor | Stores in magnetic field | Current changes | Henry (H) |
| Capacitor | Stores in electric field | Voltage changes | Farad (F) |

### 🗂️ Network classification
Active/Passive (source?) · Unilateral/Bilateral (diode?) · Linear/Non-linear (diode?) · Lumped/Distributed

### ⚡ AC vs DC
| | DC | AC |
|---|---|---|
| Direction | Fixed | Reverses periodically |
| Frequency | 0 | 50 Hz (India) |
| Voltage change | Hard | Easy (transformer) |
| Use | Phones, EV batteries, electronics | Grid, home supply |

**Why AC for transmission:** step-up → high V → low I → low I²R losses → step-down near users.

### 🏭 Power system flow
Generation (11 kV) → Step-up transformer → HV transmission → Substation → Distribution transformer → Consumer (230 V, 50 Hz)

### 🔬 Semiconductors
| Device | Terminals | Key use |
|---|---|---|
| Diode | 2 | One-way current, rectifier, LED, Zener |
| BJT | 3 (B, E, C) | Current-controlled; amplification |
| JFET | 3 (G, D, S) | Voltage-controlled, high input impedance |
| MOSFET | 3 (G, D, S) | Insulated gate, fast + low power → digital ICs |

- **Conductor** (copper) · **Insulator** (glass) · **Semiconductor** (silicon — controllable by doping)
- **Moore's Law:** transistors on a chip double about every 2 years (now slowing).

### 🌱 Energy sources
Renewable: solar (PV effect, daytime), wind (blades → generator, fluctuating), biomass (controllable, needs feedstock).
Storage (batteries, pumped hydro) balances solar/wind variation. **Home → rooftop solar + battery. EV → battery.**
""",
    "Unit 3": """
### 🧱 Materials
| Material | Key property | Typical use |
|---|---|---|
| Medium carbon steel | Strong, tough, heat treatable | Shafts |
| Alloy steel (Ni, Cr, Mo) | Stronger and tougher | Heavily loaded parts |
| Grey cast iron | Cheap, castable, damps vibration | Engine blocks, machine beds |
| Stainless steel | Corrosion resistant, costly | Corrosive environments |
| Titanium alloy (Ti-6Al-4V) | Light, strong, creep resistant | Jet engines, aerospace |
| Nickel alloys | Strength at highest temperature | Turbine blades |
| Aluminium / magnesium alloys | High strength-to-weight | Aircraft structures |

- **Cast iron:** 2–3.5 % C, brittle, strong in compression · **Steel:** up to 1.2 % C, tough, strong in tension
- **Ferrous** (iron-based, heavy, rusts, cheap) vs **non-ferrous** (no iron, light, corrosion resistant, costly)
- Selection criteria: strength, weight, cost, service temperature — balance all.

### 🏗️ Processes — pick the right one
| Need | Process |
|---|---|
| Complex shape, few parts | Sand casting |
| Many identical small parts | Die casting |
| High fatigue strength (connecting rod, crankshaft) | Forging |
| Cylindrical surface | Turning (lathe) |
| Flat / slab surface | Shaping or milling |
| Holes | Drilling → reaming / boring |
| Superior finish, tight tolerance | Grinding (≈ 0.002 mm) |
| Permanent structural joint | Arc welding |
| Removable joint | Bolting |

### ⚖️ Quick comparisons
- **Casting vs forming:** molten into mould, complex shapes, some waste **vs** solid shaped by force, simpler shapes, almost no waste
- **Forging vs casting:** fewer defects, better fatigue strength **vs** blowholes possible, complex shapes easy
- **Sand vs die casting:** cheap tooling, slow, small batches **vs** costly die, fast, mass production

### 🛠️ Machining defects
| Defect | Cause | Remedy |
|---|---|---|
| Wrong size | Tool wear, wrong setting | Replace tool, reset |
| Rough surface | Blunt tool, high feed | Sharpen, reduce feed |
| Chatter | Vibration | Rigid setup |
| Size change | Heat | Coolant |

**Lathe operations to draw:** facing, turning, taper turning, drilling, threading, knurling.

### 🤖 Smart manufacturing
Sensors + real-time data + automation → predict breakdowns, reject bad parts, less downtime.
Digital manufacturing (CAD/CAM, simulation) fixes errors before production. AI → defect detection + predictive maintenance.
""",
}
