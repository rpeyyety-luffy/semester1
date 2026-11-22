# All the questions and answers for the website.
# Each unit is a list of questions. Each question is a tuple of 3 things:
#   (question number, question text, answer)
# The answer is written in Markdown (numbered lists, tables, **bold**),
# which Streamlit turns into nicely formatted text on the page.
# "(corrected)" marks places where the original notes were incomplete or wrong.

UNIT_TITLES = {
    "Unit 1": "The Connected World — Communication, Networks & Computing",
    "Unit 2": "Power, Circuits and Electrical World",
    "Unit 3": "Materials, Machines and Manufacturing",
}


def level_of(no):
    """Q1-10 = Apply, Q11-20 = Analyze, Q21-30 = Evaluate."""
    if no <= 10:
        return "L3 – Apply"
    if no <= 20:
        return "L4 – Analyze"
    return "L5 – Evaluate"


# ---------------------------------------------------------------- UNIT 1
UNIT1 = [
    (1, "Apply the principles of communication to explain how information is transferred from a source to a destination using a suitable example.", """
1. **Communication** – transferring information from a source to a destination through a channel.
2. Five elements – sender, message, medium or channel, receiver and an agreed method of interpretation.
3. Sender and receiver must agree on how information is represented and interpreted.
4. Example – microphone converts sound into electrical signals → phone represents the sound as digital data → network carries the data → receiving phone reconstructs audible sound.
"""),
    (2, "Illustrate how computer networking enables two computers to exchange data and information.", """
1. **Computer networking** – a group of interconnected devices that exchange information and share resources.
2. Devices need network interfaces, a communication medium, suitable addressing and common rules.
3. Example: in a college lab, computers are connected to a switch with Ethernet cables; the switch forms a LAN.
4. A protocol defines the format of the message, order of messages, how the sender is identified and what happens on an error.
5. Client–server: the client sends a request to the server, the server processes it and sends a response.
"""),
    (3, "Apply the concept of internetworking to explain how two separate computer networks can communicate with each other.", """
1. **Internetworking** – linking different networks so information can cross network boundaries.
2. Independent networks are joined using routers.
3. Internet Protocol (IP) helps packets move between these diverse systems.
4. Routers inspect the destination address and use routing tables to decide the next hop.
5. The Internet is a global network of networks, not a single centrally owned network.
"""),
    (4, "Explain how the Internet of People and the Internet of Things enable connectivity, giving one practical example of each.", """
1. **Internet of People** – connectivity for human activities such as email, YouTube, video meetings and social media.
2. **Internet of Things** – extends this to sensors, machines, vehicles and appliances that exchange data and may take action automatically.
3. Example (IoP) – messaging, websites and social platforms.
4. Example (IoT) – smart watches, CCTV, smart lights, automated irrigation systems.
"""),
    (5, "Apply the working principle of an IoT system to design a smart temperature-monitoring system for a room.", """
1. **Sensor** – a temperature sensor provides a measurement.
2. **Controller** – an ESP32 reads the value and compares it with a programmed threshold.
3. **Connectivity** – the ESP32 sends the reading through Wi-Fi to the router / cloud dashboard so the user can see it remotely. *(corrected — sentence was cut off in the notes)*
4. **Action** – if the temperature exceeds the safe limit, the controller can switch on a fan or an alarm.
"""),
    (6, "Select suitable sensors for a smart watch, automatic streetlight and smart irrigation system. Justify the selection for each application.", """
1. A **sensor** converts physical quantities into electrical or digital signals.
2. Smartwatch – heart-rate sensor – to measure the health of the person.
3. Automatic streetlight – optical (light) and motion sensors – the light switches on when it is dark and a person passes.
4. Smart irrigation system – soil-moisture sensor – to ensure that the soil does not get dry.
"""),
    (7, "Illustrate the role of sensors, controllers and connectivity in an IoT-based smart irrigation system.", """
1. **Sensor** – a soil-moisture sensor measures moisture (dryness).
2. **Controller** – an ESP32 compares the reading with the chosen threshold.
3. **Action** – if the soil is too dry, it activates a relay that powers a pump or opens a valve.
4. **Connectivity** – the reading can be sent to a cloud dashboard through Wi-Fi, allowing remote supervision.
"""),
    (8, "Apply the IoT data-processing sequence to explain how a smartwatch can monitor heart rate and notify a user when necessary.", """
1. **Sensor** – the sensor measures the heart rate.
2. It sends the information to the smartphone via Bluetooth.
3. The phone uploads it via Wi-Fi or cellular data.
4. A cloud application stores the data, detects patterns and sends a notification.
"""),
    (9, "Explain how a router, Internet connection and cloud platform can be used to transmit and process data collected by an IoT device.", """
1. A gateway or router connects a local device to the Internet.
2. Example – an irrigation controller uses Wi-Fi to reach a router, which passes the data through an ISP to a cloud service.
3. The Internet carries the data to the cloud service.
4. The cloud stores the data, creates patterns and graphs, sends notifications and delivers control commands.
"""),
    (10, "Apply the IoT closed-loop concept to develop a simple automatic control system for watering plants when the soil becomes dry.", """
1. Soil-moisture sensor measures moisture and the controller compares the reading to the threshold.
2. If the soil is too dry, the controller sends a command to the relay to power the water pump or open the valve.
3. When moisture reaches the required level, the controller sends a command to stop watering.
4. **Closed loop** – the sensor measures the result of the action and the controller adjusts.
"""),
    (11, "Differentiate between communication, telecommunication and computer communication with suitable examples.", """
| Point | Communication | Telecommunication | Computer communication |
|---|---|---|---|
| Meaning | Transferring information from a source to a destination through a channel | Communicating over a long distance using a technical medium | Information represented as bits carried over a network |
| Example | Speech, text and images | Telegraph, telephone, radio, television | Video call, voice note, sensor reading |
| Key point | Sender and receiver agree on interpretation | Extends communication over distance | Same network carries text, messages, images, video |
"""),
    (12, "Analyze the differences between a computer network, internetworking and the Internet.", """
| Point | Computer network | Internetworking | Internet |
|---|---|---|---|
| Meaning | Group of interconnected devices that exchange information and share resources | Linking different networks so information crosses network boundaries | Worldwide system of interconnected networks |
| Device / rule | Switch, Ethernet (LAN) | Router | TCP/IP protocol suite |
| Example | Lab computers, printer | LAN connected to another network by a router | Home, university, mobile ISP |
"""),
    (13, "Compare the Internet of People and the Internet of Things in terms of connected entities, information exchanged and applications.", """
| Point | Internet of People | Internet of Things |
|---|---|---|
| Connected entities | People | Sensors, machines, vehicles |
| Information exchanged | Human communication, messages, websites, social platforms | Data from things; may take action automatically |
| Applications | Email, social media | Smartwatches, smart lights, irrigation |
"""),
    (14, "Analyze the roles of sensors, controllers and actuators in an IoT system. Explain how they work together.", """
1. **Sensor** – converts a physical quantity into an electrical or digital representation; alone it does not understand the measurement or decide.
2. **Controller** – reads the sensor output and executes instructions.
3. **Actuator** – produces a physical effect after a command.
4. Together: "the sensor observes, the controller decides and the actuator acts."
"""),
    (15, "Analyze the sequence of operations in an IoT system, from sensing a physical condition to performing an action.", """
1. Observe the condition (sensor).
2. Process the measurement (controller).
3. Communicate useful data (Wi-Fi).
4. Make a decision.
5. Take action or inform a user.
6. All of this works together in a closed loop.
"""),
    (16, "Compare the functions of a router, Internet connectivity and cloud platforms in an IoT-based monitoring system.", """
| Point | Router | Internet connectivity | Cloud platform |
|---|---|---|---|
| Function | Forwards IP packets between networks; connects local devices to the Internet | Carries data (through an ISP) to remote services | Remotely accessible computing service |
| Does | Passes device data out of the local network | Links the router to the cloud service | Stores readings, creates graphs, detects patterns, sends notifications and commands |
| Example | Irrigation controller → Wi-Fi → router | Router → ISP | Cloud dashboard |
"""),
    (17, "Analyze the differences between sensing, data processing, data analysis and actuation in an IoT application.", """
| Stage | What happens | Done by |
|---|---|---|
| Sensing | Physical quantity → electrical or digital signal | Sensor |
| Data processing | Reads value, applies logic, compares with threshold | Controller |
| Data analysis | Stores history, detects patterns, large-scale analysis | Cloud |
| Actuation | Produces a physical effect after a command | Actuator |
"""),
    (18, "Examine the operation of a smart irrigation system and identify the role of each component in the process of automatic watering.", """
1. **Soil-moisture sensor** – measures moisture.
2. **Controller (ESP32)** – compares reading with threshold; decides if watering is required.
3. **Relay** – switches power to the pump.
4. **Water pump / valve** – supplies or controls water flow.
"""),
    (19, "Analyze how a smart lighting system uses sensor data and control actions to operate automatically.", """
1. Not explained as a separate example in the notes; build it from these points only:
2. Optical sensors respond to light; motion sensors detect movement.
3. The controller reads sensor output and applies logic.
4. Actuators include relays and lights; a relay switches electrical power.
"""),
    (20, "Analyze the development of electronic communication from the telegraph and telephone to modern computer-based communication.", """
1. Messengers and written letters came first; the telegraph transmitted coded electrical signals.
2. Telephone – made two-way voice communication practical.
3. Radio enabled wireless broadcasting; television combined sound and moving pictures.
4. Digital communication – information (text, voice, images, video) is represented as bits and carried over computer networks and the Internet. *(corrected — point was unfinished in the notes)*
"""),
    (21, "Evaluate the importance of computer networking in enabling information exchange and collaboration. Support your answer with suitable examples.", """
1. Networks let devices exchange information and share resources (computers, printers).
2. Packet switching lets many users share network links efficiently.
3. Client–server: a server can support many clients at the same time.
4. Networking is essential for information exchange and collaboration.
"""),
    (22, "Assess the benefits of connecting physical devices through IoT compared with operating them independently.", """
1. IoT turns physical measurements into information or control.
2. Remote supervision through a dashboard (connected irrigation).
3. Concerns: cloud dependence, reliability if the Internet is interrupted, privacy and security.
4. **Verdict:** connected devices produce real-world value when sensed information leads to a meaningful response.
"""),
    (23, "Evaluate the suitability of an IoT-based smart irrigation system for reducing unnecessary water use. Justify your assessment.", """
1. Waters only when the soil is too dry (compared with a threshold).
2. Stops watering when moisture reaches the required level.
3. Closed loop: sensor measures the result and the controller adjusts.
4. **Verdict:** suitable; water is supplied only when needed.
"""),
    (24, "A manufacturing unit wants to monitor machine temperature continuously. Evaluate the suitability of an IoT-based monitoring system for this application.", """
1. Temperature sensor + controller compares with a safe limit; can activate a fan or send an alert.
2. Industrial PLCs (Programmable Logic Controllers) are designed for reliable automation and control in factories.
3. Industrial safety sensors may need a decision immediately, so processing near the device reduces response time.
4. **Verdict:** suitable, with local processing for immediate action and the cloud for history.
"""),
    (25, "Evaluate the importance of cloud platforms in storing, processing and analyzing data generated by IoT devices.", """
1. **Storage:** documents, images, videos, sensor logs, databases.
2. **Computation:** runs applications, analyses data, runs AI models.
3. **Limitations:** delays, bandwidth, cost, Internet dependence, privacy; so local (edge) processing complements the cloud.
4. **Verdict:** cloud is valuable for history and large-scale analysis, not for every immediate action.
"""),
    (26, "Assess the suitability of automatic sensor-based lighting compared with manually operated lighting for an educational building.", """
1. Not covered as a separate topic in the notes; only these points apply:
2. Sensors (optical, motion) + controller + relay can switch lights automatically.
3. IoT gives convenience and resource utilization through automated actions.
4. Manual lighting needs a person to act; an IoT closed loop acts on sensed information.
5. Automatic sensor-based lighting is suitable for offices and industry.
6. Manual operation can be cheaper in colleges where few people stay after 6 pm.
7. A college has many classrooms, labs, corridors, washrooms → large waste with manual switches.
8. Rooms are empty between lectures → automatic switch-off saves energy.
9. Corridors at night → light only when someone passes.
10. Works as a closed loop: light + motion sensor → controller → relay → light.
11. Limitations: may switch off when students sit still; needs correct sensor placement.
"""),
    (27, "Evaluate the importance of selecting appropriate sensors for the reliability and effectiveness of an IoT system. Give suitable examples.", """
1. **Why it is important:**
    - The sensor is the first stage of the IoT chain – every later decision depends on it.
    - Wrong / inaccurate sensor → wrong decision → wrong action.
    - A sensor only measures; the controller can't tell if the reading itself is wrong.
    - A good controller, network or cloud cannot fix bad data.
2. **Selection criteria:**
    - Measures the correct physical quantity.
    - Accuracy and reliability.
    - Low power for battery devices (wearables).
    - Suits the environment (heat, rain, soil, factory).
    - Cost, size and compatibility with the controller.
3. **Examples:**
    - Smart irrigation: soil-moisture sensor; using only a temperature sensor would water wet soil.
    - Smartwatch: accurate heart-rate sensor; a poor one gives false or missed alarms.
    - Streetlight: light (+ motion) sensor; a wrong sensor keeps lights ON in daytime.
    - Factory: industrial temperature sensor; a weak sensor may fail in heat and miss overheating.
"""),
    (28, "A smart monitoring system detects an abnormal condition but fails to notify the user. Evaluate the possible stages of the IoT system where the failure may have occurred.", """
1. **Sensing / controller:** measurement not processed or threshold logic not acting.
2. **Communication:** Wi-Fi, Bluetooth or cellular link not delivering data.
3. **Gateway / router or ISP:** data not reaching the Internet.
4. **Cloud:** not storing, detecting or sending notifications.
5. **Phone / user notification step:** message not delivered.
"""),
    (29, "Assess the effectiveness of an IoT closed-loop system in providing automatic control compared with a system that only displays sensor readings.", """
| Point | Closed-loop system | Display-only system |
|---|---|---|
| Action | Acts on the physical world (relay, pump, valve) | Only informs users through dashboards |
| Feedback | Sensor measures the result of the action; controller adjusts | No adjustment |
| Consistency | Consistent, 24×7 | Person may miss readings |
| Human effort | Less | High |
| Response time | Fast – automatic *(corrected — was swapped in the notes)* | Slow – depends on a human |
| Example | Smart irrigation | Readings on a dashboard |
"""),
    (30, "Evaluate how IoT-based connectivity and automated actions can improve monitoring, resource utilization and convenience in everyday life. Support your answer with suitable applications.", """
1. **Monitoring:** wearables send health measurements; smart-city sensors communicate with control centres.
2. **Resource use:** smart irrigation waters only when needed.
3. **Convenience:** dashboards, alerts, remote supervision.
4. **Concern:** more connected devices increase the importance of cybersecurity.
5. **Automation:** no human effort – pump / fan / lights work automatically.
6. **Smart city:** coordinated systems – ambulance green corridor.
7. **Healthcare:** remote monitoring – wearable → cloud → doctor.
"""),
]

# ---------------------------------------------------------------- UNIT 2
UNIT2 = [
    (1, "A 12 V battery is connected to a resistance of 6 Ω. Calculate the current flowing through the circuit using Ohm's law.", """
*(corrected — the notes only listed the formula)*

- Given: V = 12 V, R = 6 Ω
- Formula: **V = I × R  →  I = V / R**
- I = 12 / 6 = **2 A**
"""),
    (2, "An electrical appliance operates at 230 V and draws a current of 5 A. Calculate its electrical power consumption.", """
*(corrected — the notes only listed the formula)*

- Given: V = 230 V, I = 5 A
- Formula: **P = V × I**
- P = 230 × 5 = **1150 W = 1.15 kW**
"""),
    (3, "A 100 W electric bulb operates for 5 hours daily. Calculate the electrical energy consumed in one day in kWh.", """
*(corrected — the notes only listed the formula)*

- Given: P = 100 W = 0.1 kW, t = 5 h
- Formula: **E = P × t**
- E = 0.1 × 5 = **0.5 kWh** (0.5 units per day)
"""),
    (4, "Apply the concept of resistance to explain how a resistor protects an LED from excessive current in an electrical circuit.", """
1. Resistance is the opposition to current.
2. A resistor is added to deliberately reduce or control the current in the circuit.
3. An LED connected directly to a battery may draw too much current → overheats and gets damaged.
4. Resistor in series with LED → by Ohm's law (I = V/R), higher R → lower current.
5. Extra energy is dissipated as heat in the resistor, not in the LED.
6. Same current flows through resistor and LED (series loop).
"""),
    (5, "Illustrate the functioning of a capacitor as an energy storage element with a suitable circuit diagram.", """
1. **Capacitor:** stores energy as charge separation in an electric field when voltage is applied across it.
2. **Capacitance:** ability to store charge in measurable terms.
3. Its effect is felt only when the voltage across it changes.
4. **Circuit:** Battery → Switch → Resistor → Capacitor → back to Battery (+ LED/load across capacitor).
5. **Charging:** switch ON → charge collects on plates → capacitor voltage rises to battery voltage. [Outside notes]
6. **Storing:** energy held in the electric field.
7. **Discharging:** battery removed → capacitor supplies stored energy to LED/load for a short time. [Outside notes]
8. **Behaviour:** very fast charge/discharge, small total energy.
9. **Examples:** camera flash (charges in a second, releases in a second); fixed capacitors in robotics; variable capacitors in analog communication.
"""),
    (6, "Apply the concept of electrical network classification to classify circuits containing a battery, diode, resistor and capacitor.", """
1. Circuit: battery + diode + resistor + capacitor.
2. Presence of source → **ACTIVE**: has a battery (energy source).
3. Direction of current → **UNILATERAL**: diode's response depends on direction of current.
4. Linearity → **NON-LINEAR**: diode is a non-linear element (resistor and capacitor alone are linear).
5. Separability → **LUMPED**: elements can be physically separated.
6. Comparison: only resistor + capacitor → passive, bilateral, linear, lumped.
7. Comparison: battery + resistor → active, bilateral, linear.
"""),
    (7, "Explain how a transformer is used to step up voltage during electrical power transmission.", """
1. A transformer transfers energy between coils using magnetic coupling.
2. Works with changing magnetic fields → naturally an AC device.
3. Generated voltage (~11 kV) is stepped up to high voltage for transmission.
4. Secondary coil has more turns than primary → higher voltage. [Outside notes]
5. Higher voltage → lower current for the same power.
6. Lower current → lower resistive heating losses in lines.
7. Near users, step-down transformers reduce voltage (e.g. 230 V) for safe use.
8. Generator (11 kV) → Step-up transformer → HV transmission → Step-down → Consumer.
"""),
    (8, "Apply the working principle of solar cells to explain how solar energy is converted into electrical energy.", """
1. Sunlight falls on photovoltaic (PV) cells (made of semiconductor, e.g. silicon).
2. The photovoltaic effect directly produces electrical energy (DC).
3. Light energy frees charges in the cell, creating current. [Outside notes]
4. Cells are connected into modules and arrays for more power.
5. Power electronics condition the output for a local load or the grid.
6. Battery storage can be added for use beyond sunlight hours.
7. Sunlight → PV cells → Modules / arrays → Power electronics → Load / Grid (+ Battery).
8. Features: abundant, low operating emissions · works only in daytime · needs large space · dust, shading and temperature affect output.
"""),
    (9, "Explain the application of a diode in a circuit where current is required to flow only in one direction.", """
1. **Diode:** two-terminal semiconductor device that permits current mainly in one direction.
2. P-N junction diode is a non-linear, unilateral element.
3. Forward bias → conducts; reverse bias → blocks. [Outside notes]
4. **Applications:**
    - Rectifier: converts AC → unidirectional (DC-like) output, e.g. phone charger (followed by filtering + regulation).
    - Reverse-polarity protection: blocks current if a battery is connected the wrong way.
    - LED: power indicator, seven-segment display.
    - Photodiode: alarm and counter circuits.
    - Zener diode: keeps constant voltage in reverse bias (voltage stabilizer).
    - AC input → Diode (rectifier) → Filter → Regulator → DC output.
"""),
    (10, "Apply the concept of MOSFET to explain its role as an electronic switching device in a digital circuit.", """
1. MOSFET = Metal-Oxide-Semiconductor Field-Effect Transistor.
2. Three terminals: Gate (G), Drain (D), Source (S).
3. Insulated gate → gate voltage controls the channel (like a water tap); almost no gate current.
4. Gate signal ON → channel conducts → current flows → logic 1.
5. Gate signal OFF → very little current → logic 0.
6. Can switch billions of times per second.

**Why suited to digital circuits:**

7. Fast switching and low power consumption.
8. Very high input impedance (higher than JFET).
"""),
    (11, "Differentiate between EMF, voltage and potential difference with suitable examples.", """
| Basis | EMF | Potential difference |
|---|---|---|
| Meaning | Electrical force that causes electrons to move in a particular direction | Difference of potential between any two points of a circuit |
| Where | Property of the source (battery, generator) | Across any element (resistor, bulb) |
| Relation | EMF = V + internal resistance drop | V = EMF – internal drop |
| Value | Slightly higher | Slightly lower when current flows [Outside notes] |
| Open circuit | Exists | Exists even with zero current |
| Example | 1.5 V cell's EMF | Voltage across a bulb / LED |
"""),
    (12, "Analyze the relationship between voltage, current and resistance using Ohm's law. Explain the effect of increasing resistance on current.", """
1. **Voltage (V):** electrical push (like water pressure).
2. **Current (I):** rate of flow of charge (like water flow rate).
3. **Resistance (R):** opposition to flow (like a narrow pipe).
4. V ↑, R constant → I ↑ (direct relation).
5. R ↑, V constant → I ↓ (inverse relation).

**Effect of increasing resistance:**

6. Current decreases.
7. E.g. 12 V: 6 Ω → 2 A; 12 Ω → 1 A. [Outside notes]
8. Used to protect LEDs and limit current.
9. Resistance converts electrical energy into heat.
"""),
    (13, "Compare resistor, inductor and capacitor based on their energy storage or dissipation characteristics and applications.", """
| Basis | Resistor (R) | Inductor (L) | Capacitor (C) |
|---|---|---|---|
| Energy | Dissipates as heat | Stores energy with current flow (magnetic field) | Stores energy as charge separation (electric field) |
| Effect felt when | Always | Current changes | Voltage changes |
| Unit | Ohm (Ω) | Henry (H) | Farad (F) |
| Types | Fixed, rheostat, potentiometer, trim-pot | Fixed / variable | Fixed, variable; polar / non-polar |
| Applications | LED protection, volume control, signal levels | Transformers, filters, chokes | Camera flash, robotics, analog communication |
"""),
    (14, "Differentiate between AC and DC circuits based on waveform, direction of current, frequency and practical applications.", """
| Basis | DC | AC |
|---|---|---|
| Definition | Varies in magnitude only | Varies in magnitude and direction |
| Waveform | Steady / unidirectional line | Sinusoidal, alternating above and below zero |
| Direction | Essentially fixed | Reverses periodically |
| Frequency | Zero | 50 Hz in India |
| Source | Batteries, solar cells | Electrical grid, generators |
| Voltage change | Not easy | Easy using transformers |
| Applications | Phones, electronics, EV batteries | Grid transmission & distribution, home supply |
"""),
    (15, "Analyze the advantages of AC over DC for long-distance electrical power transmission.", """
1. Easy voltage transformation using transformers (step up / step down).
2. Higher voltage → lower current for the same power.
3. Lower current → lower resistive (heating) losses in conductors.
4. Economical over long distances (thinner conductors [Outside notes]).
5. Suitable for large interconnected power systems (grids).
6. Simple, robust AC switchgear and protection.
7. AC generation and distribution are well established worldwide.
8. Step-up → High V, low I → Low losses → Step-down near users.
"""),
    (16, "Differentiate between renewable and non-renewable energy sources with suitable examples and environmental considerations.", """
| Basis | Renewable | Non-renewable |
|---|---|---|
| Meaning | Replenished naturally on a human timescale | Finite reserves, formed over long geological periods |
| Example | Solar, wind, hydro, biomass, geothermal | Coal, petroleum, natural gas, nuclear fuels |
| Availability | Depends on geography, climate, season, time of day | Controllable, available on demand |
| Environment | Low operating emissions | Greenhouse gases (fossil fuels); nuclear waste issues |
| Infrastructure | Growing; needs storage & flexible grid | Well established |
| Energy density | Dilute / fluctuating (wind, solar) | High for some fuels |
| Sustainability | Sustainable | Will run out |
"""),
    (17, "Analyze the differences between solar, wind and biomass energy sources based on their working principles and availability.", """
| Basis | Solar | Wind | Biomass |
|---|---|---|---|
| Source | Sunlight | Moving air | Organic material (crop / forest residue, waste) |
| Working | PV cells → photovoltaic effect → electricity | Blades → rotor → shaft → generator → electricity | Feedstock → conversion → heat, biogas, electricity |
| Availability | Daytime only; weather dependent | Depends on wind; fluctuating | More controllable generation |
| Storage need | Yes (night) | Yes (irregular) | Less |
| Advantages | Abundant, low emissions | No fuel, low maintenance | Uses waste (waste-to-energy) |
| Limitations | Large space; dust, shading | Noisy, large machines | Feedstock collection, transport; emissions |
"""),
    (18, "Analyze the major stages of an electrical power system from generation to transmission and distribution with a block diagram.", """
**Block diagram:**

`Generation (11 kV) → Step-up Transformer → Transmission (HV) → Substation → Distribution Transformer → Consumers (230 V)`

1. **Generation:**
    - Power plants convert primary energy into electricity (thermal, hydro, nuclear, wind, solar).
    - Generated at about 11 kV.
2. **Transmission:**
    - Voltage stepped up to high voltage.
    - Moves bulk power over long distances.
    - High V → low I → low losses.
3. **Substation:**
    - Steps voltage down; provides switching, protection, control.
4. **Distribution:**
    - Local network feeds neighbourhoods, campuses, factories.
    - Distribution transformer gives 230 V, 50 Hz to homes.
    - Consumer: meter → building wiring → loads (lights, motors, chargers).
"""),
    (19, "Differentiate between conductors, insulators and semiconductors based on their electrical properties and engineering applications.", """
*(corrected — the Insulator and Semiconductor columns were swapped in the notes)*

| Basis | Conductor | Insulator | Semiconductor |
|---|---|---|---|
| Charge movement | Moves easily | Does not move easily | Between the two; controllable |
| Resistance | Very low | Very high | Medium – changes with doping |
| Examples | Copper | Glass | Silicon, germanium, gallium |
| Control | Not controllable | Not controllable | Modified by doping |
| Application | Wires, cables | Cable coating, supports | Diodes, transistors, ICs, solar cells |
"""),
    (20, "Compare diode, transistor, FET and MOSFET based on their basic functions and applications in electronic circuits.", """
| Basis | Diode | BJT (transistor) | FET (JFET) | MOSFET |
|---|---|---|---|---|
| Terminals | 2 | 3: B, E, C | 3: G, D, S | 3: G, D, S |
| Function | One-way current | Switching & amplification | Voltage-controlled current | Fast switching, insulated gate |
| Control | – | Small base current | Gate voltage | Gate voltage |
| Feature | Non-linear | Building block of electronics | Unipolar, high input impedance, low noise | Higher input impedance, low power |
| Applications | Rectifier, LED, photodiode, Zener | Switches, audio amps, oscillators | Buffer amps, RF, sensor interfaces | Processors, memory, power converters |
"""),
    (21, "Evaluate the suitability of AC and DC systems for electrical power transmission and distribution. Justify your answer with engineering reasons.", """
1. **Criteria:** voltage conversion, losses, cost, interconnection, protection, end use.

| Criterion | AC system | DC system |
|---|---|---|
| Voltage change | Easy – transformers | Not easy [Outside notes] |
| Transmission losses | Low (step up → low current) | Higher in conventional systems |
| Large interconnected grids | Suitable | Less suitable |
| Switchgear / protection | Simple, robust | Complex |
| Electronics / batteries | Must be converted | Used directly |

2. **Justification:**
    - Power travels long distances → high voltage needed → only practical with transformers → AC.
    - High V → low I → low resistive losses → economical.
    - Phones, ICs, EV batteries need controlled DC → chargers convert AC → DC.
    - History: AC won the "War of Currents" because of transformers.
3. **Conclusion:** use AC for the grid and DC for devices.
"""),
    (22, "A residential building requires an alternative source of electrical energy. Evaluate solar, wind and biomass energy sources and recommend a suitable option with justification.", """
1. **Judgment:** rooftop solar + battery is the best option for a home.
2. **Comparison:**
    - Solar: uses rooftop, silent [Outside notes], no fuel, low emissions.
    - Wind: noisy, needs large machines – unsuitable.
    - Biomass: needs regular feedstock collection and storage.
    - Battery covers night-time use.
3. **Limitations:** solar works only in daytime; dust and shading reduce output.
4. **Justification:** a home has roof space but not room for wind turbines or biomass fuel.
"""),
    (23, "Evaluate the suitability of a battery and capacitor for energy storage in an electric vehicle. Justify your selection.", """
1. **Judgment:** a battery is the suitable main storage for an EV.
2. **Comparison:**
    - Battery: high energy, long-duration supply (water tank).
    - Capacitor: very fast but stores little energy (water balloon).
    - EV runs on a DC battery charged from an AC socket or DC fast charger.
    - Capacitor only helps with short power bursts.
3. **Limitations:** battery charges slower; cost and lifetime matter.
4. **Justification:** an EV must run for hours – only a battery stores that much energy.
"""),
    (24, "A circuit is experiencing excessive current, resulting in overheating of components. Evaluate the use of different resistance values to control current and protect the circuit.", """
1. **Evaluation:**
    - I = V/R → higher R → lower current.
    - Too low R: current still high.
    - Correct R: safe current, circuit works.
    - Too high R: circuit may not work.
2. **Limitations:** the resistor itself heats up – needs a proper power rating; wastes some energy.
3. **Justification:** the same principle is used to protect LEDs.
"""),
    (25, "Evaluate the importance of power grids in ensuring reliable electricity supply to industries and residential consumers.", """
1. **Benefits:**
    - Reliability: other plants supply if one fails.
    - Power transfer between areas as demand changes.
    - Economical use of different sources.
    - Protection: relays, breakers, reserves stop faults spreading.
2. **Limitations:** risk of blackout cascade; needs constant balancing.
3. **Justification:** industries need uninterrupted power – an isolated plant can't guarantee it.
"""),
    (26, "Assess the advantages and limitations of renewable energy sources compared with non-renewable energy sources for sustainable power generation.", """
1. **Judgment:** renewables are better for sustainability.
2. **Advantages:**
    - Naturally replenished vs finite fossil reserves.
    - Low emissions vs greenhouse gases.
    - No fuel dependence (solar, wind).
3. **Limitations:** variable output, need storage and large space; non-renewables are controllable and well established.
4. **Justification:** sustainability needs sources that don't run out or pollute.
"""),
    (27, "Evaluate the role of semiconductor technology and Moore's Law in the development of modern electronic devices.", """
1. **Role:**
    - Doped silicon → transistor = controllable switch (0/1).
    - Transistors → logic gates → processors, memory (ICs).
    - Moore's Law: transistors double ~every 2 years → more power, lower cost.
    - Enables phones, cameras, AI in small devices.
2. **Limitations:** Moore's Law is slowing – leakage, heat, quantum effects.
3. **Justification:** a phone today outperforms old room-sized computers.
"""),
    (28, "A digital electronic circuit requires a semiconductor device for high-speed switching. Evaluate the suitability of a BJT and MOSFET for this application.", """
1. **Judgment:** MOSFET is more suitable for high-speed switching.
2. **Comparison:**
    - MOSFET: voltage-controlled, insulated gate, very high input impedance.
    - MOSFET: fast switching, low power – used extensively in ICs.
    - BJT: needs base current → more power and heat.
    - BJT: better for amplification.
3. **Limitations:** MOSFET has a maximum V-I rating (600 V / 200 A).
4. **Justification:** digital chips need billions of fast, low-power switches.
"""),
    (29, "Evaluate the role of energy storage systems in managing variations in electricity generation from solar and wind energy sources.", """
1. **Judgment:** energy storage is essential for using solar and wind reliably.
2. **Role:**
    - Stores surplus energy, releases it during shortfall.
    - Handles sudden changes (fast storage) and night/low-wind periods.
    - Options: batteries, pumped hydro, capacitors, hydrogen.
3. **Limitations:** no single technology fits all; also needs forecasting and a flexible grid.
4. **Justification:** solar stops at night and wind is irregular, but demand continues.
5. **Conclusion:** storage plays a key role in balancing renewables.
"""),
    (30, "Assess the importance of integrated circuits in modern electronic systems compared with circuits constructed using individual electronic components.", """
1. **Judgment:** ICs are far more important than discrete-component circuits.
2. **Advantages:**
    - Billions of devices on one tiny chip.
    - Lower cost per function, higher reliability [Outside notes].
    - Faster and more power-efficient.
    - Found in laptops, phones, routers, ACs.
3. **Limitations:** heat management; costly fabrication; hard to repair [Outside notes].
4. **Justification:** "The breakthrough is not one transistor – it is integration."
5. **Conclusion:** ICs are indispensable for modern electronics.
"""),
]

# ---------------------------------------------------------------- UNIT 3
UNIT3 = [
    (1, "Apply the principles of engineering materials selection to select a suitable material for a component subjected to high mechanical loads. Justify your selection based on material properties.", """
- High-load parts like shafts need high strength and toughness.
- Medium carbon steel is suitable as it is strong and heat treatable.
- For heavier loads, alloy steel (Ni, Cr, Mo) is stronger and tougher.
"""),
    (2, "Select suitable ferrous materials for manufacturing a machine shaft and an engine cylinder block. Justify your choices based on their properties and applications.", """
- **Shaft:** medium carbon steel, as it is strong, tough and heat treatable.
- **Cylinder block:** grey cast iron, as it is cheap and easy to cast.
- Grey cast iron also resists wear and damps vibration.
"""),
    (3, "Apply the concept of material properties to identify a suitable material for a jet engine component operating at elevated temperatures. Give reasons for your selection.", """
- Jet engine parts must stay strong at high temperature and resist creep.
- Titanium alloys (Ti-6Al-4V) are light, strong and creep resistant.
- Nickel alloys are used in the hottest parts like turbine blades.
"""),
    (4, "Illustrate the application of casting technology in manufacturing a component with a complex shape. Identify a suitable casting process and justify its use.", """
- Casting pours molten metal into a mould to get the shape.
- Sand casting suits complex parts like engine blocks, as cores form internal passages.
- It is low cost and works for almost any metal.
"""),
    (5, "Apply the principles of metal forming to select a suitable forming process for manufacturing a connecting rod. State the reasons for your selection.", """
- Forging is best for a connecting rod.
- It gives uniform grain flow and removes internal voids.
- This gives high strength against fatigue and impact loads.
"""),
    (6, "Select an appropriate subtractive manufacturing process to produce a component requiring accurate dimensions and a good surface finish. Explain its application.", """
- Turning on a lathe gives the near-final size.
- Grinding then gives high accuracy and a smooth finish.
- Grinding is used for shafts and bearing surfaces (tolerance up to 0.002 mm).
"""),
    (7, "Apply the principles of joining processes to select a suitable method for joining two metal plates used in a structural application. Justify your choice.", """
- Arc welding is best for structural plates.
- It forms a strong, rigid and permanent joint.
- Welded structures are lighter than riveted or bolted ones.
"""),
    (8, "Identify a suitable manufacturing process for producing a large number of identical metal components. Explain how the process meets production requirements.", """
- Die casting suits large numbers of identical parts.
- Metal is forced into a reusable die, so every part is the same.
- It is fast, accurate and needs little machining.
"""),
    (9, "Apply quality control principles to identify corrective actions when manufactured components do not meet specified dimensional tolerances.", """
- Measure rejected parts to find the error pattern [Outside notes].
- Check tool wear, machine setting and clamping [Outside notes].
- Replace tools, reset the machine and inspect regularly [Outside notes].
"""),
    (10, "Illustrate how sensors, data collection and automation can be applied to improve the efficiency of a manufacturing operation.", """
- Sensors measure temperature, vibration and part size [Outside notes].
- Data is monitored in real time to spot problems early [Outside notes].
- Automation adjusts machines and rejects bad parts, reducing downtime [Outside notes].
"""),
    (11, "Analyze the differences between ferrous and non-ferrous engineering materials with respect to properties, characteristics and engineering applications.", """
| Basis | Ferrous | Non-ferrous |
|---|---|---|
| Main element | Iron is the main element | Iron is absent |
| Weight | Heavy | Many are light (Al, Ti) |
| Corrosion | Most rust easily | Resist corrosion |
| Cost | Cheap | Costlier |
| Uses | Structures and machines | Aircraft and electrical wires |
"""),
    (12, "Compare cast iron and steel in terms of carbon content, mechanical properties, manufacturability and applications.", """
| Basis | Cast iron | Steel |
|---|---|---|
| Carbon | 2–3.5% carbon | Up to 1.2% carbon |
| Properties | Brittle but strong in compression | Tough and strong in tension |
| Manufacturing | Easy to cast | Easy to forge and weld |
| Uses | Machine beds, engine blocks | Shafts, gears, bridges |
"""),
    (13, "Analyze the relationship between material properties and operating conditions in selecting materials for aerospace components.", """
| Condition | Property needed | Material |
|---|---|---|
| Low weight | High strength-to-weight ratio | Aluminium and magnesium alloys |
| High temperature | Creep resistance | Nickel and titanium alloys |
| Vibration | High fatigue strength | Titanium alloys |
| Corrosive air | Corrosion resistance | Titanium and aluminium alloys |
"""),
    (14, "Differentiate between casting and metal forming processes with respect to manufacturing principles, component geometry, material utilization and applications.", """
| Basis | Casting | Metal forming |
|---|---|---|
| Principle | Molten metal is poured into a mould | Solid metal is shaped by force |
| Shape | Complex shapes are possible | Simpler shapes like rods and sheets |
| Material use | Some metal is wasted | Almost wasteless |
| Uses | Engine blocks, pump bodies | Crankshafts, rails, wires |
"""),
    (15, "Analyze the suitability of sand casting and die casting for manufacturing components in small and large production quantities.", """
| Basis | Sand casting | Die casting |
|---|---|---|
| Mould | Broken after each use | Reused many times |
| Cost | Tooling cost is low | Die cost is high |
| Speed & accuracy | Slow and less accurate | Fast and accurate |
| Best for | Small quantities, large parts | Large quantities, small parts |
"""),
    (16, "Compare forging and casting in terms of component quality, mechanical properties, production limitations and applications.", """
| Basis | Forging | Casting |
|---|---|---|
| Quality | Very few defects | May have blowholes |
| Strength | Strong under fatigue | Weaker under impact |
| Limitation | Complex shapes are difficult | Complex shapes are easy |
| Uses | Crankshafts, gears | Engine blocks, pump bodies |
"""),
    (17, "Analyze the differences between machining and joining processes in terms of their purpose, process characteristics and applications in manufacturing.", """
| Basis | Machining | Joining |
|---|---|---|
| Purpose | Removes material | Connects parts |
| Process | A cutting tool removes chips | Heat, pressure or fasteners are used |
| Examples | Turning, drilling, grinding | Welding, brazing, bolting |
| Uses | Shafts, holes, smooth surfaces | Frames, bridges, assemblies |
"""),
    (18, "Examine the possible causes of dimensional inaccuracies and surface defects in machined components. Suggest appropriate corrective measures.", """
| Defect | Cause | Remedy |
|---|---|---|
| Wrong size | Tool wear or wrong setting | Replace tool, reset machine |
| Rough surface | Blunt tool or high feed | Sharpen tool, reduce feed |
| Chatter marks | Vibration of tool or machine | Use a rigid setup |
| Size change | Heat from cutting | Use coolant |
"""),
    (19, "Analyze how quality control feedback can help identify process variations and reduce manufacturing defects.", """
- Parts are measured and results are fed back to the process [Outside notes].
- This shows when parts start drifting out of limits [Outside notes].
- The cause is corrected early, so defects and scrap reduce [Outside notes].
"""),
    (20, "Analyze the role of smart manufacturing and digital manufacturing in improving productivity, process monitoring and product quality for any one manufacturing process as an example (Casting/Forming/Machining).", """
| Area | Smart manufacturing | Digital manufacturing |
|---|---|---|
| Productivity | Breakdowns are predicted early | Setup time is reduced by CAD/CAM |
| Monitoring | Sensors track tool wear in real time | Simulation checks the process first |
| Quality | Bad parts are removed automatically | Design errors are fixed before production |
"""),
    (21, "Evaluate the suitability of stainless steel, alloy steel and cast iron for a machine component exposed to different service conditions. Justify the most appropriate choice.", """
- Stainless steel resists corrosion but is costly.
- Alloy steel is strong and tough under heavy loads.
- Cast iron is cheap but brittle in tension.
- **Judgment:** alloy steel is best, as it can be heat treated for high strength.
"""),
    (22, "Assess the importance of material selection criteria such as strength, weight, cost and service temperature in the design of an engineering component.", """
- Strength ensures the part carries its load safely.
- Low weight saves fuel in aircraft and vehicles.
- Cost and service temperature decide practicality and heat resistance.
- **Judgment:** all criteria must be balanced to avoid failure or high cost.
"""),
    (23, "Evaluate the suitability of casting and forging for manufacturing a highly loaded automotive component. Recommend the preferred process with justification.", """
- Casting is cheap but internal defects can cause failure.
- Forging gives aligned grain flow and higher fatigue strength.
- **Recommendation:** forging, as safety-critical parts need maximum strength.
"""),
    (24, "Assess the advantages and limitations of sand casting and die casting for mass production of metal components. Recommend a process for a specified production requirement.", """
- Sand casting is cheap and flexible but slow and less accurate.
- Die casting is fast and accurate, but the die is costly.
- In mass production, die cost is spread over many parts.
- **Recommendation:** die casting for mass-producing small aluminium parts.
"""),
    (25, "Evaluate the suitability of welding, bolted joints and other appropriate joining methods for assembling a structural component. Justify your recommendation.", """
- Welding gives strong, rigid and lighter joints.
- Bolting allows dismantling but can loosen under vibration [Outside notes].
- **Recommendation:** welding for permanent structures; bolting for removable parts.
"""),
    (26, "Evaluate the selection of appropriate machining process for manufacturing a component requiring (a) Cylindrical shapes, (b) Rectangular Slab shapes, (c) Holes (d) a superior surface finish. Justify each parameter. Draw schematics representation of Lathe machine operations.", """
- **(a) Cylindrical:** turning, as rotating work gives round surfaces.
- **(b) Rectangular slab:** shaping or milling, as they cut flat surfaces.
- **(c) Holes:** drilling, then reaming or boring for accuracy.
- **(d) Superior finish:** grinding, for very fine tolerance.
- Draw lathe operations: facing, turning, taper turning, drilling, threading, knurling.
"""),
    (27, "Assess the effectiveness of quality control techniques in reducing rejection rates and improving manufacturing consistency. Support your answer with an engineering example.", """
- Quality control finds defects early and keeps the process in limits [Outside notes].
- Example: regular shaft diameter checks catch tool wear early [Outside notes].
- It adds inspection cost [Outside notes].
- **Judgment:** highly effective, as preventing rejects is cheaper than scrapping.
"""),
    (28, "Evaluate the benefits and limitations of introducing robotics and industrial automation into a conventional manufacturing facility.", """
- Robots work fast and accurately, raising productivity [Outside notes].
- They improve safety in welding and painting [Outside notes].
- They are costly and need skilled maintenance [Outside notes].
- **Judgment:** worth it for high-volume, repetitive work.
"""),
    (29, "Justify whether artificial intelligence and data-driven monitoring should be implemented for defect detection and predictive maintenance in a manufacturing plant.", """
- AI detects defects faster than humans [Outside notes].
- Predictive maintenance fixes machines before breakdown [Outside notes].
- It needs data, setup cost and skilled staff [Outside notes].
- **Judgment:** yes, as savings exceed the cost.
"""),
    (30, "Evaluate the role of digital manufacturing and smart manufacturing technologies in improving productivity, quality and resource utilization.", """
- Digital manufacturing reduces errors through simulation [Outside notes].
- Smart manufacturing monitors machines in real time [Outside notes].
- Both save material and energy but need investment [Outside notes].
- **Judgment:** they play a key role in efficient manufacturing.
"""),
]

# Put everything in one dictionary the app can use.
UNITS = {
    "Unit 1": UNIT1,
    "Unit 2": UNIT2,
    "Unit 3": UNIT3,
}
