import gradio as gr

# Fonction pour calculer le prix de vente
def calculate_selling_price(kms_Driven, Present_Price, Fuel_Type, Seller_Type, Transmission, Age):
    # Calcul du prix de base
    selling_price = Present_Price * 0.8 


    # Ajustements selon le type de carburant
    if Fuel_Type == "Diesel":
        selling_price += 500
    elif Fuel_Type == "Electric":
        selling_price += 2000  # Bonus pour les voitures électriques

    # Ajustements selon le type de vendeur
    if Seller_Type == "Individual":
        selling_price -= 1000

    # Ajustements selon la transmission
    if Transmission == "Automatic":
        selling_price += 2000

    # Ajustements pour l'âge et les kilomètres
    selling_price -= (kms_Driven * 0.02)  
    selling_price -= (Age * 500)         

    # Retourner un prix minimal de 0
    return max(selling_price, 0)

# Interface Gradio
iface = gr.Interface(
    fn=calculate_selling_price,
    inputs=[
        gr.Number(label="Kilometers Driven"),
        gr.Number(label="Present Price (in $)"),
        gr.Dropdown(["Diesel", "Petrol", "Electric"], label="Fuel Type"),
        gr.Dropdown(["Dealer", "Individual"], label="Seller Type"),
        gr.Dropdown(["Manual", "Automatic"], label="Transmission"),
        gr.Number(label="Age of the Car (in years)"),
    ],
    outputs=gr.Number(label="Estimated Selling Price (in $)"),
    title="Car Selling Price Estimator",
    description="Provide details about the car to estimate its selling price.",
)

# Lancer l'application
iface.launch()

