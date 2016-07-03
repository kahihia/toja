'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('main', {
    url: '/',
    templateUrl: 'views/main.html',
    controller: 'MainCtrl as ctrl',
    resolve: {
      venues: function(Venue) {
        return Venue.query();
      },
      attractions: function(Attraction) {
        return Attraction.query();
      }
    }
  });

})
.controller('MainCtrl', function (venues, attractions) {
  var foodPriceRangeOptions = [
    {
      min: 0,
      max: 9999999,
      label: 'Any price'
    },
    {
      min: 0,
      max: 2000,
      label: 'Less than $20'
    },
    {
      min: 2001,
      max: 5000,
      label: 'From $21 to $50'
    },
    {
      min: 5001,
      max: 9999999,
      label: 'More than $51'
    }
  ];

  this.foodTab = {
    priceRangeOptions: foodPriceRangeOptions,
    priceRange: foodPriceRangeOptions[0]
  };

  this.venues = venues;
  this.attractions = attractions;

  this.venueLimit = 5;
  this.attractionLimit = 5;
});
