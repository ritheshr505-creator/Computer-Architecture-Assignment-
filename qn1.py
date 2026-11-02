
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

// Function to print an 8-bit integer in 2's complement binary format
void print_binary(int8_t val) {
    for (int i = 7; i >= 0; i--) {
        int bit = (val >> i) & 1;
        printf("%d", bit);
    }
}

// Function to perform 8-bit signed addition and detect overflow
int8_t add_8bit(int8_t a, int8_t b, bool *overflow) {
    int16_t raw_sum = (int16_t)a + (int16_t)b;
    
    // Overflow occurs if operands have the same sign and the result has a different sign
    *overflow = (a > 0 && b > 0 && raw_sum < 0) || (a < 0 && b < 0 && raw_sum >= 0);
    
    return (int8_t)raw_sum;
}

// Function to evaluate signed arithmetic expressions (+ or -)
void evaluate_expression(int8_t a, char op, int8_t b) {
    int8_t result = 0;
    bool overflow = false;
    
    if (op == '+') {
        result = add_8bit(a, b, &overflow);
    } else if (op == '-') {
        // Subtraction is implemented as a + (-b)
        // Check edge case where -(-128) exceeds the positive 8-bit signed range (+127)
        if (b == -128) {
            overflow = true;
            result = 0;
        } else {
            int8_t neg_b = -b;
            result = add_8bit(a, neg_b, &overflow);
        }
    }
    
    // Display outputs
    if (op == '+') {
        printf("Expression: %d + (%d)\n", a, b);
    } else {
        printf("Expression: (%d) - (%d)\n", a, b);
    }
    
    printf("  Operand A (%4d): ", a);
    print_binary(a);
    printf("\n");
    
    printf("  Operand B (%4d): ", b);
    print_binary(b);
    printf("\n");
    
    printf("  Result Binary : ");
    print_binary(result);
    printf("\n");
    
    printf("  Result Decimal: %d\n", result);
    printf("  Overflow      : %s\n", overflow ? "YES ⚠️" : "NO ✓");
    printf("---------------------------------------------\n");
}

int main() {
    printf("=== 8-Bit 2's Complement Arithmetic Verification ===\n\n");
    
    // Expression 1: +48 + (+23)
    evaluate_expression(48, '+', 23);
    
    // Expression 2: (-46) - (-29)
    evaluate_expression(-46, '-', -29);
    
    return 0;
}
