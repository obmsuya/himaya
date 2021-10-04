let p_arrray = [];
let b_array = [];
let r_array = [];
var geo;
let congeo;
let tanzania;
//let tz;
let road;
var selections = [];
let map;
let constid;
$(document).ready(function() {
    let consts = L.featureGroup();
    let winners = [];
    let fname;
    let lname;
    let votestotal;
    let thecount = 4; //parties
    function randombetween(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    }
    // return  array of random votes
    function generate(max, thecount) {
        var r = [];
        var currsum = 0;
        for (var i = 0; i < thecount - 1; i++) {
            r[i] = randombetween(1, max - (thecount - i - 1) - currsum);
            currsum += r[i];
        }
        r[thecount - 1] = max - currsum;
        return r;
    }

    function checkBounds(marker) {
        if (L.latLngBounds(swCorner, neCorner).contains(marker)) {
            return true;
        } else {
            return false;
        }
    }

    let buildings = L.layerGroup();
    let roads = L.layerGroup();
    let tz = L.layerGroup();
    let rg = L.layerGroup();
    let rr = L.layerGroup();
    let pres = L.layerGroup();
    let ds = L.layerGroup();
    let con = L.layerGroup();
    let wd = L.layerGroup();
    let wd_const = L.layerGroup();
    var selection;
    var selectedLayer;

    var m;
    let votes = [];
    let con_array = {};
    let wd_array = {};
    let reg_array = {}

    // function to eliminate duplicates in an array 
    function uniq(a) {
        return Array.from(new Set(a));
    }

    function arrayRemove(arr, value) {

        return arr.filter(function(ele) {
            return ele != value;
        });

    }

    function getPolygonColor(winerarray) {
        var i;
        var v = 0;
        var color;
        for (i = 0; i < winerarray.length; i++) {
            var win = winerarray[i].split('#')

            if (parseInt(win[2]) > v) {
                v = parseInt(win[2]);
                color = win[3];
                //console.log (v+""+ color); 

            }
        }

        return color;
    }

    function indexOflargest(a) {
        return a.indexOf(Math.max.apply(Math, a));
    }
    //rearrange array     
    Array.prototype.move = function(from, to) {
        this.splice(to, 0, this.splice(from, 1)[0]);
    };

    function checkTicK(ind, t) {

        return ind === t ? "<span class=\"glyphicon glyphicon-check\" style=\"color:red\"></span>" : "";

    }

    // let url = "http://10.10.6.107:8081/geoserver/bongo/wms";
    // let constlayer = L.tileLayer.wms(url, {
    //     layers: 'bongo:pres_winners_geo'

    // });

    var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZGF2aWRrYSIsImEiOiJjanh5bHp1cWYwYXMwM2Jtdmc4aW1pazBsIn0.EAfNj4ZRn1V5atLW75Cq8A';

    var osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib = 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    let osm = new L.TileLayer(osmUrl, {
        attribution: osmAttrib
    });

    let grayscale = L.tileLayer(mbUrl, {
            id: 'mapbox.light',
            attribution: mbAttr
        }),
        streets = L.tileLayer(mbUrl, {
            id: 'mapbox.streets',
            attribution: mbAttr
        });

    map = L.map('map', {
        center: [-6.821000, 39.276505],
        zoom: 14,

        layers: [rg, con,rr,osm],
        fullscreenControl: true,
        fullscreenControlOptions: {
            position: "topleft", // optional
            title: "Show me fullscreen  Map!",
            titleCancel: "Exit fullscreen mode"

        }

    });

    let baseMaps = {
        "Grayscale": grayscale,
        "Streets": streets
        //'OSM': osm

    };

    var highlight = {
        'color': '#149c14',
        'weight': 4,
        'opacity': 1
    };


    //total votes
 $.getJSON('../regcenter', function(data2) {
       rr.clearLayers();
       var geojson = L.geoJson(data2, {
                            // style: function(feature) {
                            //     return {
                            //         'color': 'brown',
                            //         'weight': 4,
                            //         'opacity': 0.5
                            //     };
                            // },

                            onEachFeature: function(feature, layer) {
                                // $("#selectconstituent").append("<option value=\'" + feature.properties.constid + "\'>" + feature.properties.const+"</ option>");
                                rr.addLayer(layer);
                              con_array[parseInt(feature.properties.reg_centre)] = layer;
                                layer.on('mouseover', function(e) {
                                    
                                    layer.bindPopup("<h6>" + feature.properties.reg_centre+"</h6>");
                                    this.openPopup();
                                });
                                layer.on('mouseout', function(e) {
                                    
                                    this.closePopup();
                                });

                            } // second oneachfeature endi
                        }); // second var geojson

        });

 

    //Regions
    

    function zoomToFeature(e) {
        map.fitBounds(e.target.getBounds());
    }

    function hideLayers(D) {
        D.eachLayer(function(layer) {
            if (!layer.feature.properties.highlight) {
                map.removeLayer(layer);
            }
        });
    }

    function showLayers(D) {
        D.eachLayer(function(layer) {
            layer.feature.properties.highlight = false;
            map.addLayer(layer);
        });
    }

    $.getJSON('../get_regional_votes_geo', function(data) {
        rg.clearLayers();
        $("#selectregion option").remove();
        $("#selectregion").append("<option value=\"0\"> --Select-- </option>");
        var geojson = L.geoJson(data, {
            style: {
                "color": "#A9A9A9",
                "weight": 8,
                "fillColor": "",
                "fillOpacity": 0
            },
            onEachFeature: function(feature, layer) {
                reg_array[parseInt(feature.properties.regionid)] = layer;
                rg.addLayer(layer);
                $("#selectregion").append("<option value=\'" + feature.properties.regionid + "\'>" + feature.properties.region_nam + "</ option>");
                layer.on('mouseover', function(e) {
                    layer.bindPopup("<h6>" + feature.properties.region_nam + "<br>" + "Pop:" + feature.properties.votes + "</h6>");
                    this.openPopup();
                });

                map.on('click', function(e) {
                    //having trouble with resetStyle, so just change it back
                    layer.setStyle({
                        'color': 'gray',
                        'weight': 3,
                        'opacity': 1
                    });
                    showLayers(geojson);
                });

                layer.on('click', function(e) {
                    this.setStyle(highlight);
                    e.target.feature.properties.highlight = true;
                    hideLayers(geojson);
                    zoomToFeature(e);

                    $("#selectregion").val(feature.properties.regionid);
                    map.fitBounds(e.target.getBounds());
                    // load constituencies
                    var region = feature.properties.region_nam;
                    $("#regname").text(region);

                    $.getJSON('../get_C_wards/?region=' + region, function(datad) {
                        con.clearLayers();
                        $("#con").show();
                        $("#selectconstituent option").remove();
                        $("#selectconstituent").append("<option value=\"0\"> --Select-- </option>");
                        var geojson = L.geoJson(datad, {
                            style: function(feature) {
                                return {
                                    'color': 'brown',
                                    'weight': 4,
                                    'opacity': 0.5
                                };
                            },

                            onEachFeature: function(feature, layer) {
                                $("#selectconstituent").append("<option value=\'" + feature.properties.const + "\'>" + feature.properties.ward_name+"</ option>");
                                con.addLayer(layer);
                                con_array[parseInt(feature.properties.ward_name)] = layer;
                                layer.on('mouseover', function(e) {
                                    this.setStyle({
                                        color: 'brown',
                                        opacity: 0.4,
                                        fillOpacity: 0.4
                                    });
                                    layer.bindPopup("<h6>" + feature.properties.ward_name+"</h6>");
                                    this.openPopup();
                                });
                                layer.on('mouseout', function(e) {
                                    this.setStyle({
                                        color: 'brown',
                                        opacity: 0.2,
                                        fillOpacity: 0.2
                                    });
                                    this.closePopup();
                                });

                            } // second oneachfeature endi
                        }); // second var geojson
                    }); // second getJSON

                }); //layer on click 
            } // first onEachFeature
        }); // first  var geojson




    }); // first getJSON

    let overlayMaps = {
       

        "Mikoa": rg,
        "Mitaa": con,
        "CRDB ATM":rr,

    };
    L.control.layers(null, overlayMaps).addTo(map); //hide base map

    // handle onchange
    $('#errordiv').hide();
    //constituency
    $('select#selectconstituent').change(function() {
        var optionSelected = $(this).find("option:selected");

        var const_id = parseInt(optionSelected.val(), 10);

        if (const_id === 0) {
            $('#errordiv').html("<p>Invalid Selection</p>");
            $('#errordiv').show();
        } else {
            $('#errordiv').empty();
            // map.setView(con_array[const_id].getLatLng(), map.getZoom());
            map.fitBounds(con_array[const_id].getBounds());
        }

    });
    //wards

    $('select#selectwards').change(function() {
        var optionSelected = $(this).find("option:selected");
        var ward_id = parseInt(optionSelected.val(), 10);

        if (ward_id === 0) {

            $('#errordiv').html("<p>Invalid Selection</p>");
            $('#errordiv').show();
        } else {
            $('#errordiv').empty();
            map.fitBounds(wd_array[ward_id].getBounds());
        }

    });
    //region
    $('select#selectregion').change(function() {
        var optionSelected = $(this).find("option:selected");
        var reg_id = parseInt(optionSelected.val(), 10);

        if (reg_id === 0) {

            $('#errordiv').html("<p>Invalid Selection</p>");
            $('#errordiv').show();

        } else { //alert("region "+reg_id);
            //map.setView(reg_array[reg_id].getLatLng(), map.getZoom());
            $('#errordiv').empty();
            map.fitBounds(reg_array[reg_id].getBounds());
        }

    }); //onchange

}); //doc ready


