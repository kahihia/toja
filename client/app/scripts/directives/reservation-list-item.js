'use strict';

/**
 * @ngdoc directive
 * @name clientApp.directive:reservationListItem
 * @description
 * # reservationListItem
 */
angular.module('clientApp')
  .directive('reservationListItem', function (
    $interval, Venue, Call, Reservation, callStatus
  ) {
    return {
      templateUrl: 'views/directives/reservation-list-item.html',
      restrict: 'E',
      scope: {
        reservation: '='
      },
      link: function postLink(scope) {
        var fetchCallStatus;

        scope.callStatus = callStatus;
        scope.venue = Venue.get({id: scope.reservation.venueId});

        scope.call = Call.get({id: scope.reservation.id});

        var timerId;

        var callDoneStates = [
          callStatus.FAILED,
          callStatus.DECLINED,
          callStatus.ACCEPTED
        ];

        scope.call.$promise.then(function() {
          scope.reservation.status = scope.call.status;
          if (callDoneStates.indexOf(scope.call.status) > -1) {
            return;
          } else {
            fetchCallStatus();
          }
        });

        fetchCallStatus = function() {
          console.debug('fetching call', scope.reservation.id);
          timerId = $interval(function() {
            scope.call = Call.get({id: scope.reservation.id});
            scope.call.$promise.then(function() {
              scope.reservation.status = scope.call.status;
              if (callDoneStates.indexOf(scope.call.status) > -1) {
                console.debug('Canceling timer');
                $interval.cancel(timerId);
                timerId = null;
              }
            });
          }, 5000);
        };

        scope.$on('$destroy', function() {
          if (timerId) {
            $interval.cancel(timerId);
          }
        });
      }
    };
  });
