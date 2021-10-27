// Indexed capitalization
package main

import (
	"strings"
)

func Capitalize(st string, arr []int) string {
	for _, ind := range arr {
		if ind < len(st) {
		st = st[:ind] + strings.ToUpper(string(st[ind])) + st[ind+1:]
		}
  	}
  return st
}
