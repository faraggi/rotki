import { BigNumber } from '@rotki/common';
import { ComputedRef, Ref } from 'vue';
import { Collateral, CollateralizedLoan } from '@/types/defi';
import { Zero } from '@/utils/bignumbers';

export const totalCollateral = (
  loan: Ref<CollateralizedLoan<Collateral<string>[]>>
): ComputedRef<BigNumber> => {
  return computed(() =>
    get(loan)
      .collateral.map(({ usdValue }) => usdValue)
      .reduce((previous, current) => previous.plus(current), Zero)
  );
};
