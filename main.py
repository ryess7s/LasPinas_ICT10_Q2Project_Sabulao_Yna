#drill 2
from pyscript import document 

def candidate_checker(e):
    club_members = ["yna sabulao", "nathan bernaldez", "kate velo", "sophie gamban", "max calata"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members
    messages = (f'Sorry {candidate}, your name is not on the list.',
                f'Congratulations {candidate}, you are now part of the Glee Club!')

    document.getElementById('result').innerHTML = messages [member_checker]

#skills test

non_metals = {
    "Hydrogen": ['H', 'Hydrogen', '1', '1.008'],
    "Helium": ['He', 'Helium', '2', '4.0026'],
    "Nitrogen": ['N', 'Nitrogen', '7', '14.007'],
    "Carbon": ['C', 'Carbon', '6', '12.011'],
    "Oxygen": ['O', 'Oxygen', '8', '15.999'],
    "Fluorine": ['F', 'Fluorine', '9', '18.998'],
    "Neon": ['Ne', 'Neon', '10', '20.180'],
    "Phosphorus": ['P', 'Phosphorus', '15', '30.974'],
    "Sulfur": ['S', 'Sulfur', '16', '32.06'],
    "Chlorine": ['Cl', 'Chlorine', '17', '35.45'],
    "Argon": ['Ar', 'Argon', '18', '39.95'],
    "Selenium": ['Se', 'Selenium', '34', '78.971'],
    "Bromine": ['Br', 'Bromine', '35', '79.904'],
    "Krypton": ['Kr', 'Krypton', '36', '83.798'],
    "Iodine": ['I', 'Iodine', '53', '126.90'],
    "Xenon": ['Xe', 'Xenon', '54', '131.29'],
    "Radon": ['Rn', 'Radon', '86', '[222]']
}

def adding_numbers(e):
    document.getElementById('result').innerHTML = ""
    element1 = document.getElementById('elements').value.strip().title()

    # Using .get() - no if statement
    info = non_metals.get(
        element1,
        ("-", "Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b> Symbol: </b> {info[0]} <br>
    <b> Element: </b> {info[1]} <br>
    <b> Atomic Number: </b> {info[2]} <br>
    <b> Atomic Mass: </b> {info[3]} <br>
    """

