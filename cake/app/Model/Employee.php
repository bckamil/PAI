<?php
App::uses('AppModel', 'Model');
/**
 * Employee Model
 *
 */
class Employee extends AppModel {
	var $validate = array(
		'nazwisko' => array(
			'notBlank' => array(
				'rule' => array('notBlank'),
				'message' => 'Pole wymagane',
			),
		),
		'etat' => array(
			'notBlank' => array(
				'rule' => array('notBlank'),
				'message' => 'Pole wymagane',
			),
		),
		'placa_pod' => array(
            'range' => array(
                'rule' => array('range', 0, 2000),
                'message' => 'Płaca podstawowa musi być w przedziale 0-2000'
            )
		)
	);
}
