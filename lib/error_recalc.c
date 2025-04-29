#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

// all the difficult code here is the original work from Neill Corlett.
// original source is cdpatch.c from cmdpack, released under the following license:
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
////////////////////////////////////////////////////////////////////////////////

int optional_form2_edc_calculated=1;

////////////////////////////////////////////////////////////////////////////////
//
// LUTs for computing ECC/EDC
//
static uint8_t  ecc_f_lut[256];
static uint8_t  ecc_b_lut[256];
static uint32_t edc_lut  [256];

static void eccedc_init(void) {
    uint32_t i, j, edc;
    for(i = 0; i < 256; i++) {
        j = (i << 1) ^ (i & 0x80 ? 0x11D : 0);
        ecc_f_lut[i    ] = (uint8_t)j;
        ecc_b_lut[i ^ j] = (uint8_t)i;
        edc = i;
        for(j = 0; j < 8; j++) {
            edc = (edc >> 1) ^ (edc & 1 ? 0xD8018001 : 0);
        }
        edc_lut[i] = edc;
    }
}

static void set32lsb(uint8_t* p, uint32_t value) {
    p[0] = (uint8_t)(value >>  0);
    p[1] = (uint8_t)(value >>  8);
    p[2] = (uint8_t)(value >> 16);
    p[3] = (uint8_t)(value >> 24);
}

////////////////////////////////////////////////////////////////////////////////
//
// Compute EDC for a block
//
static void edc_computeblock(const uint8_t* src, size_t size, uint8_t* dest) {
    uint32_t edc = 0;
    while(size--) {
        edc = (edc >> 8) ^ edc_lut[(edc ^ (*src++)) & 0xFF];
    }
    set32lsb(dest, edc);
}

////////////////////////////////////////////////////////////////////////////////
//
// Compute ECC for a block (can do either P or Q)
//
static void ecc_computeblock(
    uint8_t* src,
    uint32_t major_count,
    uint32_t minor_count,
    uint32_t major_mult,
    uint32_t minor_inc,
    uint8_t* dest
) {
    uint32_t size = major_count * minor_count;
    uint32_t major, minor;
    for(major = 0; major < major_count; major++) {
        uint32_t index = (major >> 1) * major_mult + (major & 1);
        uint8_t ecc_a = 0;
        uint8_t ecc_b = 0;
        for(minor = 0; minor < minor_count; minor++) {
            uint8_t temp = src[index];
            index += minor_inc;
            if(index >= size) index -= size;
            ecc_a ^= temp;
            ecc_b ^= temp;
            ecc_a = ecc_f_lut[ecc_a];
        }
        ecc_a = ecc_b_lut[ecc_f_lut[ecc_a] ^ ecc_b];
        dest[major              ] = ecc_a;
        dest[major + major_count] = ecc_a ^ ecc_b;