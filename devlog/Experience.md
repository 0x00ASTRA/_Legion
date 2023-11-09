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
>[Orginization](#orginization)

## Information Technology (IT)

The Information Technology category contains all of the experience reagarding all things digital. Below you can find the different attributes and their descriptions.

### Experience Table

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

## Social

## Physical

## Psycological

## Orginization