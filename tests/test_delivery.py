import unittest
from src.delivery_service import calculate_delivery_cost


class TestDeliveryService(unittest.TestCase):

    # --- УСПЕШНЫЕ ТЕСТЫ БАЗОВОЙ ЛОГИКИ ---
    def test_standard_package_normal_cost_and_date(self):
        cost, date = calculate_delivery_cost(2.0, 100, "обычный", False)
        self.assertEqual(cost, 700)
        self.assertEqual(date, "2026-09-04")

    def test_fragile_package_surcharge(self):
        cost, date = calculate_delivery_cost(2.0, 100, "хрупкий", False)
        self.assertEqual(cost, 1000)

    def test_dangerous_package_surcharge(self):
        cost, date = calculate_delivery_cost(2.0, 100, "опасный", False)
        self.assertEqual(cost, 1700)

    def test_weight_medium_category_multiplier(self):
        cost, date = calculate_delivery_cost(10.0, 100, "обычный", False)
        self.assertEqual(cost, 840)

    def test_weight_heavy_category_multiplier(self):
        cost, date = calculate_delivery_cost(25.0, 100, "обычный", False)
        self.assertEqual(cost, 1050)

    def test_invalid_weight_too_low(self):
        cost, date = calculate_delivery_cost(0.05, 100, "обычный", False)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_weight_too_high(self):
        cost, date = calculate_delivery_cost(50.1, 100, "обычный", False)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_distance_zero(self):
        cost, date = calculate_delivery_cost(5.0, 0, "обычный", False)
        self.assertEqual(cost, -1)

    def test_invalid_distance_too_high(self):
        cost, date = calculate_delivery_cost(5.0, 5001, "обычный", False)
        self.assertEqual(cost, -1)

    def test_invalid_package_type_returns_error(self):
        cost, date = calculate_delivery_cost(5.0, 100, "быстрая", False)
        self.assertEqual(cost, -1)

    def test_boundary_min_weight(self):
        cost, date = calculate_delivery_cost(0.1, 100, "обычный", False)
        self.assertEqual(cost, 700)

    def test_boundary_max_weight(self):
        cost, date = calculate_delivery_cost(50.0, 100, "обычный", False)
        self.assertEqual(cost, 1050)

    def test_boundary_min_distance(self):
        cost, date = calculate_delivery_cost(1.0, 1, "обычный", False)
        self.assertEqual(cost, 205)

    def test_boundary_max_distance(self):
        cost, date = calculate_delivery_cost(1.0, 5000, "обычный", False)
        self.assertEqual(cost, 25200)

    def test_boundary_exact_5_kg_weight(self):
        cost, date = calculate_delivery_cost(5.0, 100, "обычный", False)
        self.assertEqual(cost, 700)

    def test_boundary_exact_20_kg_weight(self):
        cost, date = calculate_delivery_cost(20.0, 100, "обычный", False)
        self.assertEqual(cost, 1050)

    # --- ТЕСТЫ, ВЫЯВЛЯЮЩИЕ ОШИБКИ (УПАДУТ НА ИСХОДНОМ КОДЕ) ---
    def test_express_delivery_cost_should_increase(self):
        """Падает: Экспресс-доставка ошибочно даёт 50% скидку вместо наценки"""
        cost, date = calculate_delivery_cost(2.0, 100, "обычный", is_express=True)
        self.assertGreater(cost, 700, "Стоимость экспресс-доставки должна быть выше базовой")

    def test_express_delivery_minimum_one_day_required(self):
        """Падает: Экспресс на короткие расстояния дает 0 дней (доставка день в день без учета минимума)"""
        cost, date = calculate_delivery_cost(2.0, 100, "обычный", is_express=True)
        self.assertEqual(date, "2026-09-04", "Срок экспресс-доставки не может быть меньше 1 дня")

    def test_string_weight_raises_error_handling(self):
        """Падает: При передаче строки возникает необработанный TypeError вместо (-1, '0000-00-00')"""
        try:
            cost, date = calculate_delivery_cost("invalid", 100, "обычный")
            self.assertEqual(cost, -1)
        except TypeError:
            self.fail("Функция вызвала TypeError вместо возврата ошибки (-1, '0000-00-00')")

    def test_distance_days_rounding_ceil(self):
        """Падает: Расстояние 999 км считается как 1 день из-за целочисленного деления // 500"""
        cost, date = calculate_delivery_cost(2.0, 999, "обычный", False)
        self.assertEqual(date, "2026-09-05", "999 км требует 2 дня доставки")


if __name__ == "__main__":
    unittest.main()