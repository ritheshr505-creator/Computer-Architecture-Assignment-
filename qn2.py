#include <stdio.h>
#include <stdint.h>


void print_binary(uint8_t val) {
    for (int i = 7; i >= 0; i--) {
        printf("%d", (val >> i) & 1);
    }
}


void ror_8bit(uint8_t val, int steps) {
    printf("--- ROR (Rotate Right without Carry) by %d positions ---\n", steps);
    printf("Original Binary: ");
    print_binary(val);
    printf("\n");

    for (int i = 1; i <= steps; i++) {
        uint8_t lsb = val & 1;
        
        val = (val >> 1) | (lsb << 7);
        
        printf("  Step %d Result: ", i);
        print_binary(val);
        printf("\n");
    }
    
    printf("Final ROR Result: ");
    print_binary(val);
    printf("\n\n");
}


void rcr_8bit(uint8_t val, int steps, uint8_t initial_carry) {
    printf("--- RCR (Rotate Right with Carry) by %d positions ---\n", steps);
    printf("Initial Carry (C): %u\n", initial_carry);
    printf("Original Binary  : ");
    print_binary(val);
    printf("\n");

    uint8_t c = initial_carry;
    for (int i = 1; i <= steps; i++) {
        uint8_t lsb = val & 1; 
        val = (val >> 1) | (c << 7);
        c = lsb;
        
        printf("  Step %d Result: C=%u, Byte=", i, c);
        print_binary(val);
        printf(" [Combined: C=%u | ", c);
        print_binary(val);
        printf("]\n");
    }
    
    printf("Final Carry      : %u\n", c);
    printf("Final RCR Result : ");
    print_binary(val);
    printf("\n\n");
}

int main() {
    
    uint8_t target_binary = 0xD5;


    ror_8bit(target_binary, 2);

    rcr_8bit(target_binary, 2, 0);

    return 0;
}

