def root(x, n):
    if x == 0:
      return 0

    low = 0
    high = max(1,x)
    mid = (low+high) / 2.0

    while (mid - low) >= 0.001:
      if pow(mid,n) > x:
        high = mid
      elif pow(mid,n) < x:
        low = mid
      else:
        break
      mid = (low+high) / 2.0
    return mid
