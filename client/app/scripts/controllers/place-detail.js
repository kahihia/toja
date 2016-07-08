'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:PlaceDetailCtrl
 * @description
 * # PlaceDetailCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('place-detail', {
    url: '/place/:id',
    templateUrl: 'views/place-detail.html',
    controller: 'PlaceDetailCtrl as ctrl',
    resolve: {
      attraction: function($stateParams, Attraction) {
        return Attraction.get({id: $stateParams.id});
      }
    }
  });

})
.controller('PlaceDetailCtrl', function ($rootScope, attraction) {
  this.map = { zoom: 15 };

  this.attraction = attraction;

  this.attraction.$promise.then(function() {
    $rootScope.navTitle = attraction.name;
  });
});
