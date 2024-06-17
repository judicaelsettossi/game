from flask import Flask, render_template, request, redirect, url_for, session

from system_alpha import System
from cle_plan_1 import liste_cle_plan_1
from cle_plan_2 import liste_cle_plan_2
from cle_plan_3 import liste_cle_plan_3
from cle_plan_4 import liste_cle_plan_4
from cle_plan_5 import liste_cle_plan_5

app = Flask(__name__)
app.secret_key = 'game'

def get_type(obj):
    return type(obj).__name__

system = System()

plans = [
    ('P1', system.plan_1, liste_cle_plan_1),
    ('P2', system.plan_2, liste_cle_plan_2),
    ('P3', system.plan_3, liste_cle_plan_3),
    ('P4', system.plan_4, liste_cle_plan_4),
    ('P5', system.plan_5, liste_cle_plan_5)
]

# Fonction pour filtrer les résultats basés sur les clés
def filtrer_resultats(plan, cles):
    resultats = {}
    for i in cles:
        for k, v in plan.items():
            if all(cle in v for cle in i):
                resultats[k] = v
    return resultats

@app.route('/')
def index():
    return render_template('index.html', plans=plans)

@app.route('/process_form', methods=['POST'])
def process_form():
    # Récupérer les données du formulaire
        poto_1 = request.form.get('poto_1')
        poto_2 = request.form.get('poto_2')
        poto_3 = request.form.get('poto_3')
        poto_4 = request.form.get('poto_4')
        poto_5 = request.form.get('poto_5')

        plan_un = system.plan_1('P1', poto_1)
        plan_deux = system.plan_2('P2', poto_2)
        plan_trois = system.plan_3('P3', poto_3)
        plan_quatre = system.plan_4('P4', poto_4)
        plan_cinq = system.plan_5('P5', poto_5)

        # Filtrage des résultats 1 pour chaque lot
        plan_un_lot_un = liste_cle_plan_1[0:5]
        resultats1_lot_un = filtrer_resultats(plan_un, plan_un_lot_un)

        plan_un_lot_deux = liste_cle_plan_1[5:15]
        resultats1_lot_deux = filtrer_resultats(plan_un, plan_un_lot_deux)

        plan_un_lot_trois = liste_cle_plan_1[15:23]
        resultats1_lot_trois = filtrer_resultats(plan_un, plan_un_lot_trois)

        # Filtrage des résultats 2 pour chaque lot
        plan_un_lot_un = liste_cle_plan_1[0:5]
        resultats2_lot_un = filtrer_resultats(plan_deux, plan_un_lot_un)

        plan_un_lot_deux = liste_cle_plan_1[5:15]
        resultats2_lot_deux = filtrer_resultats(plan_deux, plan_un_lot_deux)

        plan_un_lot_trois = liste_cle_plan_1[15:23]
        resultats2_lot_trois = filtrer_resultats(plan_deux, plan_un_lot_trois)

        # Filtrage des résultats 3 pour chaque lot
        plan_un_lot_un = liste_cle_plan_1[0:5]
        resultats3_lot_un = filtrer_resultats(plan_trois, plan_un_lot_un)

        plan_un_lot_deux = liste_cle_plan_1[5:15]
        resultats3_lot_deux = filtrer_resultats(plan_trois, plan_un_lot_deux)

        plan_un_lot_trois = liste_cle_plan_1[15:23]
        resultats3_lot_trois = filtrer_resultats(plan_trois, plan_un_lot_trois)

        # Filtrage des résultats 4 pour chaque lot
        plan_un_lot_un = liste_cle_plan_1[0:5]
        resultats4_lot_un = filtrer_resultats(plan_quatre, plan_un_lot_un)

        plan_un_lot_deux = liste_cle_plan_1[5:15]
        resultats4_lot_deux = filtrer_resultats(plan_quatre, plan_un_lot_deux)

        plan_un_lot_trois = liste_cle_plan_1[15:23]
        resultats4_lot_trois = filtrer_resultats(plan_quatre, plan_un_lot_trois)

        # Filtrage des résultats 5 pour chaque lot
        plan_un_lot_un = liste_cle_plan_1[0:5]
        resultats5_lot_un = filtrer_resultats(plan_cinq, plan_un_lot_un)

        plan_un_lot_deux = liste_cle_plan_1[5:15]
        resultats5_lot_deux = filtrer_resultats(plan_cinq, plan_un_lot_deux)

        plan_un_lot_trois = liste_cle_plan_1[15:23]
        resultats5_lot_trois = filtrer_resultats(plan_cinq, plan_un_lot_trois)

        session['resultats'] = {
            '01' : resultats1_lot_un,
            '02' : resultats1_lot_deux,
            '03' : resultats1_lot_trois,
            '04' : resultats2_lot_un,
            '05' : resultats2_lot_deux,
            '06' : resultats2_lot_trois,
            '07' : resultats3_lot_un,
            '08' : resultats3_lot_deux,
            '09' : resultats3_lot_trois,
            '10' : resultats4_lot_un,
            '11' : resultats4_lot_deux,
            '12' : resultats4_lot_trois,
            '13' : resultats5_lot_un,
            '14' : resultats5_lot_deux,
            '15' : resultats5_lot_trois
        }

        return redirect(url_for('reponse'))

@app.route('/reponse')
def reponse():
    resultats = session.get('resultats', {})
    resultat_01 = resultats.get('01', {}),
    resultat_02 = resultats.get('04', {}),
    resultat_03 = resultats.get('07', {}),
    resultat_04 = resultats.get('10', {}),
    resultat_05 = resultats.get('13', {}),

    # Passer les données à reponse.html pour affichage
    return render_template('resultat.html', resultat1=resultat_01, resultat2=resultat_02, resultat3=resultat_03, resultat4=resultat_04, resultat5=resultat_05)

if __name__ == '__main__':
    app.run(debug=True)