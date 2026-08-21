import pandas as pd
import mypkg.services.sessions as S  # adjust to match your actual loader module
import mypkg.services.file_manager as f
def Data_Conversion():
    current_user = "3564071289"  # TODO: swap back to S.get_current_user() after testing

    try:
        data = f.load_transaction()
    except (FileNotFoundError, ValueError) as e:
        raise RuntimeError(f"Could not load transaction data: {e}") from e

    if current_user not in data:
        raise ValueError(f"No transaction data found for user {current_user}")

    user_data = data[current_user]
    if not user_data:
        raise ValueError(f"User {current_user} has no transactions")

    data_frame = pd.DataFrame(user_data).T

    required_cols = {"amount", "category", "date_", "type_"}
    missing = required_cols - set(data_frame.columns)
    if missing:
        raise ValueError(f"Transaction data missing required columns: {missing}")

    data_frame["date_"] = pd.to_datetime(data_frame["date_"], errors="coerce")
    data_frame["type_"] = data_frame["type_"].str.lower().str.strip()
    data_frame["amount"] = pd.to_numeric(data_frame["amount"], errors="coerce")

    bad_types = ~data_frame["type_"].isin(["income", "expense"])
    if bad_types.any():
        raise ValueError(f"Unexpected type_ values found: {data_frame.loc[bad_types, 'type_'].unique()}")

    if data_frame[["date_", "amount"]].isna().any().any():
        raise ValueError("Some transactions have invalid date_ or amount values")

    return data_frame


def IncomeRows():
    return Data_Conversion()[Data_Conversion()["type_"] == "income"]


def ExpenseRows():
    return Data_Conversion()[Data_Conversion()["type_"] == "expense"]