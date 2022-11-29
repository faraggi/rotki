import { logger } from '@/utils/logging';

export const startPromise = <T>(promise: Promise<T>): void => {
  promise.then().catch(e => logger.debug(e));
};
