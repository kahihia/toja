'use strict';

/**
 * @ngdoc service
 * @name clientApp.callStatus
 * @description
 * # callStatus
 * Constant in the clientApp.
 */
angular.module('clientApp')
.constant('callStatus', {
  READY: 911,
  ON_CALLING: 5,
  ACCEPTED: 1,
  DECLINED: 0,
  FAILED: -1
});
