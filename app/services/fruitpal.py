#  Coco Matthey
#  https://www.linkedin.com/in/coco-matthey/

import logging

from app.services.cost import Cost
from app.services.overhead_data import OverheadData

logger = logging.getLogger(__name__)


class Fruitpal:
    def calculate(self, commodity, pricePerTon, tradeVolume, overheadData):
        """
        :param commodity: The commodity (e.g. mangos) :type: str
        :param pricePerTon: The price per ton (in dollars) :type: float
        :param tradeVolume: The trade volume (in tons) :type: float
        :param overheadData: 3rd-Party Data contains of fixed and variable overhead data :type: json
        :return: List of cost per country :type: [Cost]
        """
        if not commodity or len(commodity) == 0:
            logger.info("commodity cannot be None or empty")
            return
        pricePerTon = float(pricePerTon)
        tradeVolume = int(tradeVolume)
        # Filter overheadData down to only pertain to the commodity passed
        overheadDataWithCommodity = [o for o in overheadData if o["COMMODITY"] == commodity]
        # Add a feature to use the default when the commodity is not found
        # Get the list of coutries without the commodity passed
        allCountries = set([o["COUNTRY"] for o in overheadData])
        countriesWithCommodity = set([o["COUNTRY"] for o in overheadDataWithCommodity])
        countriesWithOutCommodity = allCountries - countriesWithCommodity
        # For countries without the commodity, use the default
        overheadDataWithoutCommodity = [o for o in overheadData
                                        if o["COMMODITY"] == "default" and o[
                                            "COUNTRY"] in countriesWithOutCommodity]  # Line 23
        overheadDataFinal = overheadDataWithCommodity + overheadDataWithoutCommodity

        costs = []
        # Iterate through the countries to calculate the cost
        for item in overheadDataFinal:
            cost = Cost(commodity, pricePerTon, tradeVolume, float(item["VARIABLE_OVERHEAD"]),
                        float(item["FIXED_OVERHEAD"]), item["COUNTRY"])
            costs.append(cost)
            # Sort costs list by price high to low
            sorted_costs = sorted(costs, key=lambda x: x.total, reverse=True)
        return sorted_costs


# For code view
if __name__ == "__main__":
    # For code view only
    # Calling by function
    mode = "FILE"
    overheadData = OverheadData(mode).overheadData
    f = Fruitpal()
    # Per code review, make the code more readable by passing the args explicitly
    costs = f.calculate(commodity="mango", pricePerTon=53, tradeVolume=405, overheadData=overheadData)
    print("\n".join(list(map(lambda c: str(c), costs))))

    # Calling by command line
    # if len(sys.argv) == 4:
    #     _, commodity, pricePerTon, tradeVolume = sys.argv
    #     costs = f.calculate(commodity, float(pricePerTon), float(tradeVolume), overheadData)
    #     print("\n".join(list(map(lambda c: str(c), costs))))
    # else:
    #     print("Usage: xxx")

    """
    Output:
    BR 22060.10 | (54.42*405)+20
    MX 21999.20 | (54.24*405)+32
    US 21871.00 | (54.00*405)+1
    """
