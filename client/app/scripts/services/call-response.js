'use strict';

/**
 * @ngdoc service
 * @name clientApp.callResponse
 * @description
 * # callResponse
 * Constant in the clientApp.
 */
angular.module('clientApp')
.constant('callResponse', {
  READY: 'We are ready to make the call.',
  ON_CALLING: 'We are in the middle of the call to the restaurant.',
  ACCEPTED: 'Reservation has been accepted.',
  DECLINED: 'Reservation has been declined.',
  FAILED: 'The call is not successful.'
});
