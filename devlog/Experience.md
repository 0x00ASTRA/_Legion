# Creating an Experience System

The experience system is a crucial part to game progression. Without it, games often feel dull. Experience systems allow the player to develop skills and unlock new abilities, items and rewards the more of the game your play. This is a deep-dive into how I designed and developed the experience system for _Legion.

## Table of Contents:

>[Information Technology](#information-technology-it)
>
>[Tactical](#tactical)
>
>[Social](#social)
>
>[Physical](#physical)
>
>[Psychological](#psycological)
>
>[Organization](#organization)

## Information Technology (IT)

The Information Technology category contains all of the experience regarding all things digital. Below you can find the different attributes and their descriptions.

### IT XP Table

| Category   | Subcategory          | Proficiency |
|------------|----------------------|-------------|
| Hacking    | Fundamentals         | 0           |
|            | Recon                | 0           |
|            | Attacks              | 0           |
|            | Exploitation         | 0           |
|            | Post Exploitation    | 0           |
|            | Stealth              | 0           |
| Programming| Fundamentals         | 0           |
|            | Paradigms            | 0           |
|            | Logic                | 0           |
|            | Control Flow         | 0           |
|            | Languages            | 0           |
|            | Language Mastery     | 0           |
|            | Data Analysis        | 0           |
| Networking | Fundamentals         | 0           |
|            | Security             | 0           |
|            | Architecture         | 0           |
|            | Redundancy           | 0           |
| Hardware   | Fundamentals         | 0           |
|            | Electrical           | 0           |
|            | Architecture         | 0           |
|            | Logic                | 0           |
|            | Efficiency           | 0           |

---

#### JSON Object:

```json
{
    "IT": {
        "hacking": {
            "fundimentals": 0,
            "recon": 0,
            "attacks": 0,
            "exploitation": 0,
            "post_exploitation": 0,
            "stealth": 0
        },
        "programming": {
            "fundimentals": 0,
            "paradigms": 0,
            "logic": 0,
            "control_flow": 0,
            "languages": 0,
            "language_mastery": 0,
            "data_analysis": 0
        },
        "networking": {
            "fundimentals": 0,
            "security": 0,
            "architecture": 0,
            "redundancy" : 0
        },
        "hardware": {
            "fundimentals": 0,
            "electrical": 0,
            "architecture": 0,
            "logic": 0,
            "efficiency": 0
        }
    }
}

```

#### Python Class:

```python
class IT(XPCategory):
    def __init__(
        self,
        hacking: Hacking,
        programming: Programming,
        networking: Networking,
        hardware: Hardware,
    ):
        self.hacking = hacking
        self.hardware = hardware
        self.programming = programming
        self.networking= networking
        self.hardware = hardware
```
---

### Hacking

>  #### *All stats related to the curious mind aka hacking.*

>```json
>"IT": {
>    "hacking": {
>        "fundimentals": 0,
>        "recon": 0,
>        "attacks": 0,
>        "exploitation": 0,
>        "post_exploitation": 0,
>        "stealth": 0
>    }
>}
>```

>```python
>class Hacking(XPStatCategory):
>    def __init__(
>        self,
>        fundimentals,
>        recon,
>        attacks,
>        exploitation,
>        post_expoitation,
>        stealth
>    ):
>        self.fundimentals = fundmentals
>        self.recon = recon
>        self.attacks = attacks
>        self.exploitation = exploitation
>        self.post_exploitation = post_exploitation
>        self.stealth = stealth
>```

#### Stats:

##### Fundimentals:

```json
"hacking": {
    "fundimentals": 0
}
```

> This aspect refers to *the **foundational knowledge** and comprehension of hacking concepts*. Similar to a character's 'General' stat in gaming, it signifies the player's understanding of core hacking principles. As the player advances or gains more experience, their fundamental skills will proportionally improve.

#### Recon:

```json
"hacking": {
    "recon": 0
}
```

> This subcategory relates to the ***preliminary phase*** in hacking, involving the acquisition of information and the assessment of a target before launching an attack. Each target typically contains specific data sets available for reconnaissance. The proficiency in recon is reflected by the number of these data sets the player can successfully gather before initiating an attack.

#### Attacks:

```json
"hacking": {
    "attacks": 0
}
```

> This segment encapsulates the player's ability to execute various types of attacks. It reflects the diversity and proficiency in employing different attack methodologies, such as DDoS attacks, social engineering, brute force attacks, or others. A higher proficiency in attacks indicates a broader arsenal and proficiency in executing diverse attack strategies.

#### Exploitation:

```json
"hacking": {
    "exploitaion": 0
}
```

> This skill area concentrates on the proficiency in exploiting identified vulnerabilities within a target. It reflects the player's capability to ***leverage weaknesses** discovered during reconnaissance* to gain unauthorized access or control. A high level of expertise in exploitation indicates a deep understanding of how to manipulate vulnerabilities for gaining access.

#### Post Exploitation:

```json
"hacking": {
    "post_exploitaion": 0
}
```

> Post exploitation refers to the phase after a successful exploitation where the player maintains control over the target system. Proficiency in post exploitation involves tasks such as maintaining access, privilege escalation, data exfiltration, or any activities performed after an initial successful breach.

#### Stealth:

```json
"hacking": {
    "stealth": 0
}
```

> The stealth skill involves the player's ability to conduct activities discreetly without leaving any traces or raising suspicion. It measures the player's competence in remaining undetected while navigating through systems, avoiding detection by security measures, or erasing any evidence of intrusion or activity.

---

### Programming:

> All stats related to programming I/O systems via a programming or scripting language.

>```json
>"IT": {
>    "programming": {
>        "fundimentals": 0,
>        "paradigms": 0,
>        "logic": 0,
>        "control_flow": 0,
>        "languages": 0,
>        "language_mastery": 0,
>        "data_analysis": 0
>    }
>}
>```

> ```python
> class Programming(XPStatCategory):
>     def __init__(
>         self,
>         fundamentals: int = 0,
>         paradigms: int = 0,
>         logic: int,
>         control_flow: int = 0,
>         languages: int = 0,
>         language_mastery: int = 0,
>         data_analysis: int = 0,
>     ):
>         self.fundamentals = fundamentals
>         self.paradigms = paradigms
>         self.logic = logic
>         self.control_flow = control_flow
>         self.languages = languages
>         self.language_mastery = language_mastery
>         self.data_analysis = data_analysis
> ```

#### **Stats**:

##### Fundimentals:

```json
"programming": {
    "fundimentals": 0
}
```

> This aspect refers to *the **foundational knowledge** and comprehension of programming concepts*. Similar to a character's 'General' stat in gaming, it signifies the player's understanding of core programming principles. As the player advances or gains more experience, their fundamental skills will proportionally improve.

##### Paradigms:

```json
"programming": {
    "paradigms": 0
}
```

> The Paradigms stat reflects the player's understanding and proficiency in different programming paradigms such as procedural, object-oriented, or functional programming. Higher proficiency indicates a broader understanding of different programming approaches, allowing for more versatile problem-solving.

##### Logic:

```json
"programming": {
    "logic": 0
}
```

> The Logic skill represents the player's ability to think logically and solve problems effectively using programming. It includes the capacity to create sound algorithms, troubleshoot, and approach issues with a logical mindset.

##### Control Flow:

```json
"programming": {
    "control_flow": 0
}
```

> The Control Flow proficiency signifies the player's mastery in structuring the sequence in which computer instructions are executed. It reflects the understanding of loops, conditionals, and branching in programming languages to control the flow of a program.

##### Languages:

```json
"programming": {
    "languages": 0
}
```

> The Languages stat represents the player character's familiarity and experience with various programming languages, including Python, JavaScript, C++, etc. It indicates the breadth of programming languages the character has exposure to.

##### Language Mastery:

```json
"programming": {
    "language_mastery": 0
}
```

> This skill assesses the depth of the player's proficiency in a specific programming language. It represents how well a player knows a particular language, potentially measured on a scale or ranking for each language.

##### Data Analysis:

```json
"programming": {
    "data_analysis": 0
}
```

> The Data Analysis proficiency reflects the player's capacity to manipulate, process, and derive insights from data using programming. It involves skills related to handling datasets, applying algorithms, and drawing conclusions from data.

---

### Networking:

> #### *All stats related to the tranfer of data between devices.*

>```json
>"IT": {
>    "networking": {
>        "fundimentals": 0,
>        "security": 0,
>        "architecture": 0,
>        "redundancy" : 0
>    }
>}
>```

>```python
> class Networking(XPStatCategory):
>    def __init__(
>        self,
>       fundimentals: int =0,
>       security: int=0,
>       architecture: int =0,
>       redundancy: int =0
>    ):
>       self.fundimentals = fundimentals
>       self.security = security
>       self.architecture = architecture
>       self.redundacy = redundancy
>```

#### Stats:

##### Fundimentals:

```json
"networking": {
    "fundimentals": 0
}
```

> The fundamentals skill in networking signifies the foundational knowledge and understanding of core networking concepts. It relates to a character's 'General' stat in gaming, indicating the player's grasp of fundamental networking principles. As the player advances or gains more experience, their fundamental networking skills will proportionally improve.

##### Security:

```json
"networking":  {
    "security": 0
}
```

> The Security proficiency in networking reflects the player's ability to comprehend and implement security measures within networks. It includes knowledge of encryption, firewalls, intrusion detection systems, and other security protocols aimed at safeguarding networks and systems from potential threats.

##### Architecture:

```json
"networking": {
    "architecture": 0
}
```

> The Architecture skill pertains to the player's understanding of network architectures, including how networks are designed, structured, and organized. It includes familiarity with various network topologies, such as LAN, WAN, or hybrid architectures, and the ability to design or optimize network layouts.

##### Redundancy:

```json
"networking": {
    "redundancy": 0
}
```

> The Redundancy proficiency in networking involves the player's knowledge and implementation of redundant systems or backups to ensure network availability and reliability. It signifies the capability to design or maintain systems that can continue operating in case of failures or disruptions.

---

### Hardware

> #### *All stats related to knowledge of electrical hardware. Ex: Motherboards, circuits, chips. etc.*

>```json
>"IT": {
>   "hardware": {
>       "fundimentals": 0,
>       "electrical": 0,
>       "architecture": 0,
>       "logic": 0, 
>       "efficiency": 0
>   }
>}
>```

>```python
>class Hardware(XPStatCategory):
>    def __ini__(
>        self,
>        fundimentals: int =0,
>        electrical: int =0,
>        architecture: int =0,
>        logic: int =0,
>        efficiency: int =0
>    ):
>       self.fundimentals = fundimentals
>       self.electrical = electrical
>       self.architecture = architecture
>       self.logic = logic
>       self.efficiency = efficiency
>
>```

#### Stats:

##### Fundimentals:

```json
"hardware": {
    "fundimentals": 0
}
```

> The Fundamentals skill in hardware denotes the foundational understanding of core hardware concepts. This skill relates to a character's 'General' stat in gaming, signifying the player's grasp of fundamental hardware principles. As the player advances or gains more experience, their fundamental hardware skills will proportionally improve.

##### Electrical:

```json
"hardware": {
    "electrical": 0
}
```

> The Electrical proficiency reflects the player's knowledge and understanding of electrical systems within hardware. It involves comprehension of circuits, components, power systems, and other electrical elements related to hardware infrastructure.

##### Architecture:

```json
"hardware": {
    "architecture": 0
}
```

> The Architecture skill in hardware signifies the player's understanding of hardware architectures. This includes knowledge about how hardware components are structured, interconnected, and organized to form systems or devices.

##### Logic:

```json
"hardware": {
    "logic": 0
}
```

> The Logic skill involves the player's ability to think logically and solve problems related to hardware systems. It includes the capability to create sound designs, troubleshoot, and approach hardware-related issues with a logical mindset.

##### Efficiency

```json
"hardware": {
    "efficiency": 0
}
```

> The Efficiency skill reflects the player's capacity to optimize and enhance the performance of hardware systems. It involves skills related to improving energy consumption, speed, or resource utilization within hardware setups.

---

## Tactical

The characters Tactical XP Category encompasses their combat proficency. How lethal is your player?

### Tactical XP Table

| Category   | Subcategory          | Proficiency |
|------------|----------------------|-------------|
| Tactics    | Strategy             | 0           |
|            | Planning             | 0           |
|            | Adaptability         | 0           |
|            | Decision-making      | 0           |
|            | Risk Assessment      | 0           |
| Combat     | Weapon Proficiency   | 0           |
|            | Close Quarters Combat| 0           |
|            | Marksmanship         | 0           |
|            | Tactical Maneuvers   | 0           |
| Survival   | Wilderness Skills    | 0           |
|            | First Aid            | 0           |
|            | Resourcefulness      | 0           |
|            | Navigation           | 0           |

### JSON Object

```json
{
    "Tactical": {
        "tactics": {
            "strategy": 0,
            "planning": 0,
            "Adaptability": 0,
            "decision_making": 0,
            "risk_assessment": 0
        },
        "combat": {
            "weapon_proficiency": 0,
            "cqb": 0,
            "hand2hand": 0,
            "marksmanship": 0,
            "tactical_maneuvers": 0
        },
        "survival": {
            "Wilderness Skills": 0,
            "First Aid": 0,
            "Resourcefulness": 0,
            "Navigation": 0
        }
    }
}
```

### Python Class

```python
class Tactical(XPCategory):
    def __init__(
        self,
        tactics: Tactics,
        combat: Combat,
        survival: Survival,
    ):
        self.tactics = tactics
        self.combat = combat
        self.survival = survival

```

### Tactics

> #### *All stats related to tactical strategies.*

>```json
>"Tactical": {
>    "tactics": {
>        "strategy": 0,
>        "planning": 0,
>        "adaptability": 0,
>        "decision_making": 0,
>        "risk_assessment": 0
>    }
>}
>```

>```python
>class Tactics(XPStatCategory):
>   def __init__(
>       self,
>       strategy: int =0,
>       planning: int =0,
>       adaptability: int =0,
>       decision_making: int =0,
>       risk_assessment: int =0
>   ):
>       self.strategy = strategy
>       self.planning = planning
>       self.adaptability = adaptability
>       self.decision_making = decision_making
>       self.risk_assessment = risk_assessment
>
>```

#### Stats

##### Strategy

```json
"tactics": {
    "strategy": 0
}
```

> This subcategory involves the player's proficiency in developing high-level strategies. It reflects the player's capability to devise plans, objectives, and methodologies, often involving long-term or overarching strategies.

##### Planning

```json
"tactics": {
    "planning": 0
}
```

> Planning represents the skill of creating specific plans and organizing actionable steps to achieve predefined goals or objectives. Proficiency in planning indicates the player's ability to break down strategies into practical steps.

##### Adaptability

```json
"tactics": {
    "adaptability": 0
}
```

> This area measures the player's ability to adjust and modify plans or strategies on the fly based on changing circumstances. A higher proficiency in adaptability indicates a better capability to swiftly adjust to unexpected situations.

##### Decision Making

```json
"tactics": {
    "decision_making": 0
}
```

> Decision-making reflects the player's capability to make swift and effective decisions within the context of the defined strategy. It showcases the proficiency in making informed and rational choices.

##### Risk Assesment

```json
"tactics": {
    "risk_assessment": 0
}
```

> This segment focuses on the player's ability to evaluate and analyze risks associated with the defined strategy. It involves assessing potential risks and implementing measures to mitigate them effectively.

---

### Combat

> #### *All stats related to Combat experience.*

>```json
>"Tactical": {
>    "combat": {
>        "weapon_proficiency": 0,
>        "cqb": 0,
>        "hand2hand": 0,
>        "marksmanship": 0,
>        "tactical_maneuvers": 0
>    }
>}
>```

>```python
>class Combat(XPStatCategory):
>   def __init__(
>       self,
>       weapon_proficiency: int =0,
>       cqb: int =0,
>       hand2hand: int =0,
>       marksmanship: int =0,
>       tactical_maneuvers: int =0
>   ):
>       self.weapon_proficiency = weapon_proficiency
>       self.cqb = cqb
>       self.hand2haand = hand2hand
>       self.marksmanship = marksmanship
>       self.tactical_maneuvers = tactical_maneuvers
>
>```

#### Stats

##### Weapon Proficiency

```json
"combat": {
    "weapon_proficiency": 0
}
```

> Weapon Proficiency represents the skill level in handling and using various types of weapons effectively. It includes mastery with diverse weapon types, such as firearms, melee weapons, or specialized tools.

##### CQB

```json
"combat": {
    "cqb": 0
}
```

> This subcategory involves expertise in fighting at close range. It signifies the player's proficiency in hand-to-hand combat, grappling, or melee combat in confined spaces.

##### Hand 2 Hand

```json
"combat": {
    "hand2hand": 0
}
```

> Hand 2 Hand refersto the player's proficiency melee combat scenarios. It aims to quantify how likely a player is to survive a fist or knife fight; All forms of bladed and melee weaopons included.

##### Marksmanship

```json
"combat": {
    "marksmanship": 0
}
```

> Marksmanship refers to the player's proficiency in using ranged weapons, especially firearms, with precision and accuracy. It reflects the player's skill in aiming and shooting at targets accurately.

##### Tactical Maneuvers

```json
"combat": {
    "tactical_maneuvers": 0
}
```

> Tactical Maneuvers represent the player's expertise in executing strategic movements or actions during combat. It encompasses skills such as flanking, suppressing fire, cover usage, or other tactical movements in combat scenarios.

---

### Survival

> #### *All stats related to the character's ability to survive in any given scenario or enviroment.*

>```json
>"Tactical": {
>    "survival": {
>        "wilderness_skills": 0,
>        "first_aid": 0,
>        "resourcefulness": 0,
>        "navigation": 0
>    }
>}
>```

>```python
>class Survival(XPStatCategory):
>   def __init__(
>       self,
>       wilderness_skills: int =0,
>       first_aid: int  =0,
>       resourcefulness: int =0,
>       navigation: int =0
>   ):
>       self.wilderness_skills = wilderness_skills
>       self.first_aid = first_aid
>       self.resourcefulness = resourcefulness
>       self.navigation = navigation
>```

#### Stats

##### Wilderness Skills

```json
"survival": {
    "wilderness_skills": 0
}
```

> Wilderness Skills encompass proficiency in surviving and thriving in natural environments. It involves knowledge of outdoor survival, shelter building, foraging, hunting, and other essential skills required in the wilderness.

##### Fist Aid

```json
"survival": {
    "first_aid": 0
}
```

> First Aid signifies the player's proficiency in providing initial medical assistance in emergency situations. It includes skills in treating wounds, administering CPR, managing injuries, or stabilizing individuals until further medical help arrives.

##### Resourcefullness

```json
"survival": {
    "resourcefullness": 0
}
```

> Resourcefulness measures the player's ability to adapt and find innovative solutions in challenging situations. It includes the ability to use available resources effectively, solve problems, and adapt to changing conditions.

##### Navigation

```json
"survival": {
    "navigation": 0
}
```

> Navigation relates to the player's capability to traverse terrains by using maps, compasses, or other navigational tools. It includes skills in orienteering, map reading, understanding coordinates, and effectively navigating through environments.

---

## Social

---

## Physical

---

## Psycological

---

## Organization