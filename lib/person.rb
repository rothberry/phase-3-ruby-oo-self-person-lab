# your code goes here

class Person
  # macros for what the USER
  attr_reader :name, :happiness, :hygiene
  # attr_writer :bank_account
  attr_accessor :bank_account
  # def hygiene
  #   @hygiene
  # end
  
  # ! ATTRIBUTE INSTANCE METHODS
  def initialize(name)
    @name = name
    @bank_account = 25
    @happiness = 8
    @hygiene = 8
  end
  
  def happiness=(new_value)
    if new_value > 10
      @happiness = 10
    elsif new_value < 0
      @happiness = 0
    else
      @happiness = new_value
    end
  end
  
  # def set_hygiene(new_value)
  def hygiene=(new_value)
    # p "hygiene setter"
    if new_value > 10
      @hygiene = 10
    elsif new_value < 0
      @hygiene = 0
    else
      @hygiene = new_value
    end
  end

  # ! NON-ATTRIBUTE INSTANCE METHODS
  def happy?
    # if @happiness > 7 
    #   return true
    # else 
    #   return false
    # end
    return @happiness > 7
  end
  
  def clean?
    # if @hygiene > 7 
    #   return true
    # else 
    #   return false
    # end
    return @hygiene > 7
  end

  def get_paid(amount)
    @bank_account += amount
    return "all about the benjamins"
  end

  def take_bath
    # @hygiene += 4
    # @hygiene = 43
    # set_hygiene(hygiene + 4)
    # self.hygiene=(hygiene + 4)
    self.hygiene = hygiene + 4
    return '♪ Rub-a-dub just relaxing in the tub ♫'
  end

  def work_out
    self.hygiene = hygiene - 3
    self.happiness = happiness + 2
    return '♪ another one bites the dust ♫'
  end

  def call_friend(friend)
    self.happiness = happiness + 3
    friend.happiness = friend.happiness + 3
    return "Hi #{friend.name}! It's #{self.name}. How are you?"
  end

  def start_conversation(friend, topic)
    if topic == "politics"
      self.happiness = happiness - 2
      friend.happiness = friend.happiness - 2  
      return "blah blah partisan blah lobbyist"
    elsif topic == 'weather'
      self.happiness = happiness + 1
      friend.happiness = friend.happiness + 1
      return "blah blah sun blah rain"
    else
      return "blah blah blah blah blah"
    end
  end

end

# lance = Person.new('lance')
# p lance
# lance.take_bath
# p lance
