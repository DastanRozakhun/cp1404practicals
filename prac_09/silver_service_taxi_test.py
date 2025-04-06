# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def test_silver_service_taxi():
    """Test the SilverServiceTaxi class."""
    # Test initialization
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
    assert fancy_taxi.name == "Hummer"
    assert fancy_taxi.fuel == 200
    assert fancy_taxi.fanciness == 4
    assert fancy_taxi.price_per_km == Taxi.price_per_km * 4
    
    # Test fare calculation with flagfall
    fancy_taxi.start_fare()
    fancy_taxi.drive(10)
    expected_fare = 10 * (Taxi.price_per_km * 4) + SilverServiceTaxi.flagfall
    assert fancy_taxi.get_fare() == expected_fare
    
    # Test specific case from requirements
    test_taxi = SilverServiceTaxi("Test", 100, 2)
    test_taxi.start_fare()
    test_taxi.drive(18)
    assert test_taxi.get_fare() == 48.78  # 18 * 1.23 * 2 + 4.50 = 48.78
    
    # Test string representation
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.start_fare()
    expected_str = f"Hummer, fuel=200, odometer=0, 0km on current fare, ${Taxi.price_per_km * 4:.2f}/km plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"    
    assert str(hummer) == expected_str
    
    print("All tests passed!")

if __name__ == '__main__':
    test_silver_service_taxi()
