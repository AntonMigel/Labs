import datetime
from tensorflow.keras import layers, models, datasets, losses, callbacks


def create_model():
    model = models.Sequential()
    model.add(layers.Flatten(input_shape=(32, 32, 3)))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    model.compile(optimizer='adam',
                  loss=losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])
    print(model.summary())
    return model


def main():
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

    train_images, test_images = train_images / 255.0, test_images / 255.0

    model = create_model()

    log_dir = 'log/{}'.format(datetime.datetime.now())
    tensor_board = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels),
                        callbacks=[tensor_board])
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(test_loss)  
    print(test_acc)  


if __name__ == '__main__':
    main()
