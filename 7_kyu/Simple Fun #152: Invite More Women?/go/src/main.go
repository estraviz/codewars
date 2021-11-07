// Simple Fun #152: Invite More Women?
package kata

func inviteMoreWomen(L []int) bool {
  if addArray(L) <= 0 {
    return false
  }
  return true
}

func addArray(L []int) int {
  var result int = 0
  for _, guest := range L {
    result += guest
  }
  return result
}
