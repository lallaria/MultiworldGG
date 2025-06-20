from .Names import SkillNames, CareerNames, AspirationNames

sims4_regions = {
    "Menu": [
        CareerNames.base_career_astronaut_2, CareerNames.base_career_astronaut_3,
        CareerNames.base_career_astronaut_4, CareerNames.base_career_astronaut_5, CareerNames.base_career_astronaut_6,
        CareerNames.base_career_astronaut_7, CareerNames.base_career_astronaut_8A, CareerNames.base_career_astronaut_8B,
        CareerNames.base_career_astronaut_9A, CareerNames.base_career_astronaut_9B,
        CareerNames.base_career_athlete_2, CareerNames.base_career_athlete_3,
        CareerNames.base_career_athlete_4, CareerNames.base_career_athlete_5B, CareerNames.base_career_athlete_5A,
        CareerNames.base_career_athlete_6A, CareerNames.base_career_athlete_6B, CareerNames.base_career_athlete_7A,
        CareerNames.base_career_athlete_7B, CareerNames.base_career_athlete_8A, CareerNames.base_career_athlete_8B,
        CareerNames.base_career_athlete_9A, CareerNames.base_career_athlete_9B,
        CareerNames.base_career_business_2, CareerNames.base_career_business_3,
        CareerNames.base_career_business_4, CareerNames.base_career_business_5, CareerNames.base_career_business_6,
        CareerNames.base_career_business_7A, CareerNames.base_career_business_7B, CareerNames.base_career_business_8A,
        CareerNames.base_career_business_8B, CareerNames.base_career_business_9A, CareerNames.base_career_business_9B,
        CareerNames.base_career_criminal_2, CareerNames.base_career_criminal_3,
        CareerNames.base_career_criminal_4, CareerNames.base_career_criminal_5, CareerNames.base_career_criminal_6A,
        CareerNames.base_career_criminal_6B, CareerNames.base_career_criminal_7A, CareerNames.base_career_criminal_7B,
        CareerNames.base_career_criminal_8A, CareerNames.base_career_criminal_8B, CareerNames.base_career_criminal_9A,
        CareerNames.base_career_criminal_9B,
        CareerNames.base_career_culinary_2, CareerNames.base_career_culinary_3,
        CareerNames.base_career_culinary_4, CareerNames.base_career_culinary_5, CareerNames.base_career_culinary_6A,
        CareerNames.base_career_culinary_6B, CareerNames.base_career_culinary_7A, CareerNames.base_career_culinary_7B,
        CareerNames.base_career_culinary_8A, CareerNames.base_career_culinary_8B, CareerNames.base_career_culinary_9A,
        CareerNames.base_career_culinary_9B,
        CareerNames.base_career_entertainer_2,
        CareerNames.base_career_entertainer_3, CareerNames.base_career_entertainer_4,
        CareerNames.base_career_entertainer_5A, CareerNames.base_career_entertainer_5B,
        CareerNames.base_career_entertainer_6A, CareerNames.base_career_entertainer_6B,
        CareerNames.base_career_entertainer_7A, CareerNames.base_career_entertainer_7B,
        CareerNames.base_career_entertainer_8A, CareerNames.base_career_entertainer_8B,
        CareerNames.base_career_entertainer_9A, CareerNames.base_career_entertainer_9B,
        CareerNames.base_career_painter_2, CareerNames.base_career_painter_3,
        CareerNames.base_career_painter_4, CareerNames.base_career_painter_5, CareerNames.base_career_painter_6,
        CareerNames.base_career_painter_7A, CareerNames.base_career_painter_7B, CareerNames.base_career_painter_8A,
        CareerNames.base_career_painter_8B, CareerNames.base_career_painter_9A, CareerNames.base_career_painter_9B,
        CareerNames.base_career_secret_agent_2,
        CareerNames.base_career_secret_agent_3, CareerNames.base_career_secret_agent_4,
        CareerNames.base_career_secret_agent_5, CareerNames.base_career_secret_agent_6,
        CareerNames.base_career_secret_agent_7, CareerNames.base_career_secret_agent_8A,
        CareerNames.base_career_secret_agent_8B, CareerNames.base_career_secret_agent_9A,
        CareerNames.base_career_secret_agent_9B, CareerNames.base_career_secret_agent_10B,
        CareerNames.base_career_style_influencer_2,
        CareerNames.base_career_style_influencer_3, CareerNames.base_career_style_influencer_4,
        CareerNames.base_career_style_influencer_5, CareerNames.base_career_style_influencer_6A,
        CareerNames.base_career_style_influencer_6B, CareerNames.base_career_style_influencer_7A,
        CareerNames.base_career_style_influencer_7B, CareerNames.base_career_style_influencer_8A,
        CareerNames.base_career_style_influencer_8B, CareerNames.base_career_style_influencer_9A,
        CareerNames.base_career_style_influencer_9B,
        CareerNames.base_career_tech_guru_2, CareerNames.base_career_tech_guru_3,
        CareerNames.base_career_tech_guru_4, CareerNames.base_career_tech_guru_5, CareerNames.base_career_tech_guru_6,
        CareerNames.base_career_tech_guru_7A, CareerNames.base_career_tech_guru_7B,
        CareerNames.base_career_tech_guru_8A, CareerNames.base_career_tech_guru_8B,
        CareerNames.base_career_tech_guru_9A, CareerNames.base_career_tech_guru_9B,
        CareerNames.base_career_writer_2, CareerNames.base_career_writer_3,
        CareerNames.base_career_writer_4, CareerNames.base_career_writer_5, CareerNames.base_career_writer_6A,
        CareerNames.base_career_writer_6B, CareerNames.base_career_writer_7A, CareerNames.base_career_writer_7B,
        CareerNames.base_career_writer_8A, CareerNames.base_career_writer_8B, CareerNames.base_career_writer_9A,
        CareerNames.base_career_writer_9B,
        CareerNames.base_ptj_barista_2, CareerNames.base_ptj_barista_3,
        CareerNames.base_ptj_babysitter_2, CareerNames.base_ptj_babysitter_3,
        CareerNames.base_ptj_fastfood_employee_2,
        CareerNames.base_ptj_fastfood_employee_3,
        CareerNames.base_ptj_manual_laborer_2,
        CareerNames.base_ptj_manual_laborer_3,
        CareerNames.base_ptj_retail_employee_2,
        CareerNames.base_ptj_retail_employee_3,
        AspirationNames.base_aspiration_basic_trainer, AspirationNames.base_aspiration_ill_at_easel,
        AspirationNames.base_aspiration_fledgelinguist, AspirationNames.base_aspiration_tone_deaf,
        AspirationNames.base_aspiration_mostly_harmless, AspirationNames.base_aspiration_villainous_valentine,
        AspirationNames.base_aspiration_readily_a_parent, AspirationNames.base_aspiration_aluminum_chef,
        AspirationNames.base_aspiration_bar_tenderfoot, AspirationNames.base_aspiration_going_for_not_broke,
        AspirationNames.base_aspiration_estate_of_the_art, AspirationNames.base_aspiration_prudent_student,
        AspirationNames.base_aspiration_with_the_program, AspirationNames.base_aspiration_amore_amateur,
        AspirationNames.base_aspiration_naturewalker, AspirationNames.base_aspiration_out_and_about,
        AspirationNames.base_aspiration_fish_out_of_water, AspirationNames.base_aspiration_practical_joker,
        AspirationNames.base_aspiration_new_in_town, AspirationNames.base_aspiration_neighborly_advisor,
        f"{SkillNames.base_skill_charisma} 1", f"{SkillNames.base_skill_charisma} 2",
        f"{SkillNames.base_skill_charisma} 3", f"{SkillNames.base_skill_charisma} 4",
        f"{SkillNames.base_skill_charisma} 5", f"{SkillNames.base_skill_charisma} 6",
        f"{SkillNames.base_skill_charisma} 7", f"{SkillNames.base_skill_charisma} 8",
        f"{SkillNames.base_skill_charisma} 9", f"{SkillNames.base_skill_charisma} 10",
        f"{SkillNames.base_skill_fitness} 1", f"{SkillNames.base_skill_fitness} 2",
        f"{SkillNames.base_skill_fitness} 3", f"{SkillNames.base_skill_fitness} 4",
        f"{SkillNames.base_skill_fitness} 5", f"{SkillNames.base_skill_fitness} 6",
        f"{SkillNames.base_skill_fitness} 7",
        f"{SkillNames.base_skill_logic} 1", f"{SkillNames.base_skill_mischief} 1",
        f"{SkillNames.base_skill_mixology} 1", f"{SkillNames.base_skill_cooking} 1",
        f"{SkillNames.base_skill_rocket_science} 1", f"{SkillNames.base_skill_photography} 1",
        f"{SkillNames.base_skill_painting} 1", f"{SkillNames.base_skill_guitar} 1",
        f"{SkillNames.base_skill_violin} 1", f"{SkillNames.base_skill_piano} 1",
        f"{SkillNames.base_skill_handiness} 1", f"{SkillNames.base_skill_programming} 1",
        f"{SkillNames.base_skill_video_gaming} 1", f"{SkillNames.base_skill_gardening} 1",
        f"{SkillNames.base_skill_fishing} 1", f"{SkillNames.base_skill_writing} 1",
        f"{SkillNames.base_skill_comedy} 1"
    ]
}

sims4_careers = {
    # Astronaut
    "astronaut": (
        CareerNames.base_career_astronaut_2,
        CareerNames.base_career_astronaut_3,
        CareerNames.base_career_astronaut_4,
        CareerNames.base_career_astronaut_5,
        CareerNames.base_career_astronaut_6,
        CareerNames.base_career_astronaut_7,

        CareerNames.base_career_astronaut_8A,
        CareerNames.base_career_astronaut_9A,
        CareerNames.base_career_astronaut_8B,
        CareerNames.base_career_astronaut_9B,
        CareerNames.base_career_astronaut_10A,
        CareerNames.base_career_astronaut_10B
    ),
    # Athlete
    "athlete": (
        CareerNames.base_career_athlete_2,
        CareerNames.base_career_athlete_3,
        CareerNames.base_career_athlete_4,

        CareerNames.base_career_athlete_5A,
        CareerNames.base_career_athlete_6A,
        CareerNames.base_career_athlete_7A,
        CareerNames.base_career_athlete_8A,
        CareerNames.base_career_athlete_9A,
        CareerNames.base_career_athlete_5B,
        CareerNames.base_career_athlete_6B,
        CareerNames.base_career_athlete_7B,
        CareerNames.base_career_athlete_8B,
        CareerNames.base_career_athlete_9B,
        CareerNames.base_career_athlete_10A,
        CareerNames.base_career_athlete_10B
    ),
    # Business
    "business": (
        CareerNames.base_career_business_2,
        CareerNames.base_career_business_3,
        CareerNames.base_career_business_4,
        CareerNames.base_career_business_5,
        CareerNames.base_career_business_6,

        CareerNames.base_career_business_7A,
        CareerNames.base_career_business_8A,
        CareerNames.base_career_business_9A,
        CareerNames.base_career_business_7B,
        CareerNames.base_career_business_8B,
        CareerNames.base_career_business_9B,
        CareerNames.base_career_business_10A,
        CareerNames.base_career_business_10B
    ),
    # Criminal
    "criminal": (
        CareerNames.base_career_criminal_2,
        CareerNames.base_career_criminal_3,
        CareerNames.base_career_criminal_4,
        CareerNames.base_career_criminal_5,

        CareerNames.base_career_criminal_6A,
        CareerNames.base_career_criminal_7A,
        CareerNames.base_career_criminal_8A,
        CareerNames.base_career_criminal_9A,
        CareerNames.base_career_criminal_6B,
        CareerNames.base_career_criminal_7B,
        CareerNames.base_career_criminal_8B,
        CareerNames.base_career_criminal_9B,
        CareerNames.base_career_criminal_10A,
        CareerNames.base_career_criminal_10B
    ),
    # Culinary
    "culinary": (
        CareerNames.base_career_culinary_2,
        CareerNames.base_career_culinary_3,
        CareerNames.base_career_culinary_4,
        CareerNames.base_career_culinary_5,

        CareerNames.base_career_culinary_6A,
        CareerNames.base_career_culinary_7A,
        CareerNames.base_career_culinary_8A,
        CareerNames.base_career_culinary_9A,
        CareerNames.base_career_culinary_6B,
        CareerNames.base_career_culinary_7B,
        CareerNames.base_career_culinary_8B,
        CareerNames.base_career_culinary_9B,
        CareerNames.base_career_culinary_10A,
        CareerNames.base_career_culinary_10B
    ),
    # Entertainer
    "entertainer": (
        CareerNames.base_career_entertainer_2,
        CareerNames.base_career_entertainer_3,
        CareerNames.base_career_entertainer_4,

        CareerNames.base_career_entertainer_5A,
        CareerNames.base_career_entertainer_6A,
        CareerNames.base_career_entertainer_7A,
        CareerNames.base_career_entertainer_8A,
        CareerNames.base_career_entertainer_9A,
        CareerNames.base_career_entertainer_5B,
        CareerNames.base_career_entertainer_6B,
        CareerNames.base_career_entertainer_7B,
        CareerNames.base_career_entertainer_8B,
        CareerNames.base_career_entertainer_9B,
        CareerNames.base_career_entertainer_10A,
        CareerNames.base_career_entertainer_10B
    ),
    "painter": (
        # Painter
        CareerNames.base_career_painter_2,
        CareerNames.base_career_painter_3,
        CareerNames.base_career_painter_4,
        CareerNames.base_career_painter_5,
        CareerNames.base_career_painter_6,

        CareerNames.base_career_painter_7A,
        CareerNames.base_career_painter_8A,
        CareerNames.base_career_painter_9A,
        CareerNames.base_career_painter_7B,
        CareerNames.base_career_painter_8B,
        CareerNames.base_career_painter_9B,
        CareerNames.base_career_painter_10A,
        CareerNames.base_career_painter_10B
    ),
    "secret_agent": (
        # Secret Agent
        CareerNames.base_career_secret_agent_2,
        CareerNames.base_career_secret_agent_3,
        CareerNames.base_career_secret_agent_4,
        CareerNames.base_career_secret_agent_5,
        CareerNames.base_career_secret_agent_6,
        CareerNames.base_career_secret_agent_7,

        CareerNames.base_career_secret_agent_8A,
        CareerNames.base_career_secret_agent_9A,
        CareerNames.base_career_secret_agent_8B,
        CareerNames.base_career_secret_agent_9B,
        CareerNames.base_career_secret_agent_10B,
        CareerNames.base_career_secret_agent_10A,
        CareerNames.base_career_secret_agent_11B
    ),
    # Style Influencer
    "style_influencer": (
        CareerNames.base_career_style_influencer_2,
        CareerNames.base_career_style_influencer_3,
        CareerNames.base_career_style_influencer_4,
        CareerNames.base_career_style_influencer_5,

        CareerNames.base_career_style_influencer_6A,
        CareerNames.base_career_style_influencer_7A,
        CareerNames.base_career_style_influencer_8A,
        CareerNames.base_career_style_influencer_9A,
        CareerNames.base_career_style_influencer_6B,
        CareerNames.base_career_style_influencer_7B,
        CareerNames.base_career_style_influencer_8B,
        CareerNames.base_career_style_influencer_9B,
        CareerNames.base_career_style_influencer_10A,
        CareerNames.base_career_style_influencer_10B
    ),
    # Tech Guru
    "tech_guru": (
        CareerNames.base_career_tech_guru_2,
        CareerNames.base_career_tech_guru_3,
        CareerNames.base_career_tech_guru_4,
        CareerNames.base_career_tech_guru_5,
        CareerNames.base_career_tech_guru_6,

        CareerNames.base_career_tech_guru_7A,
        CareerNames.base_career_tech_guru_8A,
        CareerNames.base_career_tech_guru_9A,
        CareerNames.base_career_tech_guru_7B,
        CareerNames.base_career_tech_guru_8B,
        CareerNames.base_career_tech_guru_9B,
        CareerNames.base_career_tech_guru_10A,
        CareerNames.base_career_tech_guru_10B
    ),
    # Writer
    "writer": (
        CareerNames.base_career_writer_2,
        CareerNames.base_career_writer_3,
        CareerNames.base_career_writer_4,
        CareerNames.base_career_writer_5,

        CareerNames.base_career_writer_6A,
        CareerNames.base_career_writer_7A,
        CareerNames.base_career_writer_8A,
        CareerNames.base_career_writer_9A,
        CareerNames.base_career_writer_6B,
        CareerNames.base_career_writer_7B,
        CareerNames.base_career_writer_8B,
        CareerNames.base_career_writer_9B,
        CareerNames.base_career_writer_10A,
        CareerNames.base_career_writer_10B
    )
}

sims4_aspiration_milestones = {
    "bodybuilder": (
        AspirationNames.base_aspiration_basic_trainer,
        AspirationNames.base_aspiration_exercise_demon,
        AspirationNames.base_aspiration_fit_to_a_t,
        AspirationNames.base_aspiration_bodybuilder,
    ),
    "painter_extraordinaire": (
        AspirationNames.base_aspiration_ill_at_easel,
        AspirationNames.base_aspiration_fine_artist,
        AspirationNames.base_aspiration_brushing_with_greatness,
        AspirationNames.base_aspiration_painter_extraordinaire,
    ),
    "bestselling_author": (
        AspirationNames.base_aspiration_fledgelinguist,
        AspirationNames.base_aspiration_competent_wordsmith,
        AspirationNames.base_aspiration_novelest_novelist,
        AspirationNames.base_aspiration_bestselling_author,
    ),
    "musical_genius": (
        AspirationNames.base_aspiration_tone_deaf,
        AspirationNames.base_aspiration_fine_tuned,
        AspirationNames.base_aspiration_harmonious,
        AspirationNames.base_aspiration_musical_genius,
    ),
    "public_enemy": (
        AspirationNames.base_aspiration_mostly_harmless,
        AspirationNames.base_aspiration_neighborhood_nuisance,
        AspirationNames.base_aspiration_criminal_mind,
        AspirationNames.base_aspiration_public_enemy,
    ),
    "chief_of_mischief": (
        AspirationNames.base_aspiration_mostly_harmless,
        AspirationNames.base_aspiration_artful_trickster,
        AspirationNames.base_aspiration_professional_prankster,
        AspirationNames.base_aspiration_chief_of_mischief,
    ),
    "master_chef": (
        AspirationNames.base_aspiration_aluminum_chef,
        AspirationNames.base_aspiration_captain_cook,
        AspirationNames.base_aspiration_culinary_artist,
        AspirationNames.base_aspiration_master_chef,
    ),
    "master_mixologist": (
        AspirationNames.base_aspiration_bar_tenderfoot,
        AspirationNames.base_aspiration_electric_mixer,
        AspirationNames.base_aspiration_beverage_boss,
        AspirationNames.base_aspiration_master_mixologist
    ),
    "renaissance_sim": (
        AspirationNames.base_aspiration_prudent_student,
        AspirationNames.base_aspiration_jack_of_some_trades,
        AspirationNames.base_aspiration_pantologist,
        AspirationNames.base_aspiration_renaissance_sim
    ),
    "nerd_brain": (
        AspirationNames.base_aspiration_prudent_student,
        AspirationNames.base_aspiration_erudite,
        AspirationNames.base_aspiration_rocket_scientist,
        AspirationNames.base_aspiration_nerd_brain,
    ),
    "computer_whiz": (
        AspirationNames.base_aspiration_with_the_program,
        AspirationNames.base_aspiration_technically_adept,
        AspirationNames.base_aspiration_computer_geek,
        AspirationNames.base_aspiration_computer_whiz,
    ),
    "serial_romantic": (
        AspirationNames.base_aspiration_amore_amateur,
        AspirationNames.base_aspiration_up_to_date,
        AspirationNames.base_aspiration_romance_juggler,
        AspirationNames.base_aspiration_serial_romantic,
    ),
    "freelance_botanist": (
        AspirationNames.base_aspiration_naturewalker,
        AspirationNames.base_aspiration_garden_variety,
        AspirationNames.base_aspiration_nature_nurturer,
        AspirationNames.base_aspiration_freelance_botanist,
    ),
    "the_curator": (
        AspirationNames.base_aspiration_out_and_about,
        AspirationNames.base_aspiration_gatherer,
        AspirationNames.base_aspiration_treasure_hunter,
        AspirationNames.base_aspiration_the_curator,
    ),
    "angling_ace": (
        AspirationNames.base_aspiration_fish_out_of_water,
        AspirationNames.base_aspiration_hooked,
        AspirationNames.base_aspiration_reel_smart,
        AspirationNames.base_aspiration_angling_ace,
    ),
    "joke_star": (
        AspirationNames.base_aspiration_practical_joker,
        AspirationNames.base_aspiration_standup_startup,
        AspirationNames.base_aspiration_funny,
        AspirationNames.base_aspiration_joke_star,
    ),
    "friend_of_the_world": (
        AspirationNames.base_aspiration_new_in_town,
        AspirationNames.base_aspiration_well_liked,
        AspirationNames.base_aspiration_super_friend,
        AspirationNames.base_aspiration_friend_of_the_world,
    ),
    "neighborly_advisor": (
        AspirationNames.base_aspiration_neighborly_advisor,
    )
}

sims4_skill_dependencies = {
    f"{SkillNames.base_skill_charisma} 1": ["Menu", f"{SkillNames.base_skill_charisma} 2"],
    f"{SkillNames.base_skill_charisma} 2": ["Menu", f"{SkillNames.base_skill_charisma} 3"],
    f"{SkillNames.base_skill_charisma} 3": ["Menu", f"{SkillNames.base_skill_charisma} 4"],
    f"{SkillNames.base_skill_charisma} 4": ["Menu", f"{SkillNames.base_skill_charisma} 5"],
    f"{SkillNames.base_skill_charisma} 5": ["Menu", f"{SkillNames.base_skill_charisma} 6"],
    f"{SkillNames.base_skill_charisma} 6": ["Menu", f"{SkillNames.base_skill_charisma} 7"],
    f"{SkillNames.base_skill_charisma} 7": ["Menu", f"{SkillNames.base_skill_charisma} 8"],
    f"{SkillNames.base_skill_charisma} 8": ["Menu", f"{SkillNames.base_skill_charisma} 9"],
    f"{SkillNames.base_skill_charisma} 9": ["Menu", f"{SkillNames.base_skill_charisma} 10"],

    f"{SkillNames.base_skill_fitness} 1": ["Menu", f"{SkillNames.base_skill_fitness} 2"],
    f"{SkillNames.base_skill_fitness} 2": ["Menu", f"{SkillNames.base_skill_fitness} 3"],
    f"{SkillNames.base_skill_fitness} 3": ["Menu", f"{SkillNames.base_skill_fitness} 4"],
    f"{SkillNames.base_skill_fitness} 4": ["Menu", f"{SkillNames.base_skill_fitness} 5"],
    f"{SkillNames.base_skill_fitness} 5": ["Menu", f"{SkillNames.base_skill_fitness} 6"],
    f"{SkillNames.base_skill_fitness} 6": ["Menu", f"{SkillNames.base_skill_fitness} 7"],
    f"{SkillNames.base_skill_fitness} 7": ["Menu", f"{SkillNames.base_skill_fitness} 8"],
    f"{SkillNames.base_skill_fitness} 8": ["Menu", f"{SkillNames.base_skill_fitness} 9"],
    f"{SkillNames.base_skill_fitness} 9": ["Menu", f"{SkillNames.base_skill_fitness} 10"],

    f"{SkillNames.base_skill_logic} 1": ["Menu", f"{SkillNames.base_skill_logic} 2"],
    f"{SkillNames.base_skill_logic} 2": ["Menu", f"{SkillNames.base_skill_logic} 3"],
    f"{SkillNames.base_skill_logic} 3": ["Menu", f"{SkillNames.base_skill_logic} 4"],
    f"{SkillNames.base_skill_logic} 4": ["Menu", f"{SkillNames.base_skill_logic} 5"],
    f"{SkillNames.base_skill_logic} 5": ["Menu", f"{SkillNames.base_skill_logic} 6"],
    f"{SkillNames.base_skill_logic} 6": ["Menu", f"{SkillNames.base_skill_logic} 7"],
    f"{SkillNames.base_skill_logic} 7": ["Menu", f"{SkillNames.base_skill_logic} 8"],
    f"{SkillNames.base_skill_logic} 8": ["Menu", f"{SkillNames.base_skill_logic} 9"],
    f"{SkillNames.base_skill_logic} 9": ["Menu", f"{SkillNames.base_skill_logic} 10"],

    f"{SkillNames.base_skill_mischief} 1": ["Menu", f"{SkillNames.base_skill_mischief} 2"],
    f"{SkillNames.base_skill_mischief} 2": ["Menu", f"{SkillNames.base_skill_mischief} 3"],
    f"{SkillNames.base_skill_mischief} 3": ["Menu", f"{SkillNames.base_skill_mischief} 4"],
    f"{SkillNames.base_skill_mischief} 4": ["Menu", f"{SkillNames.base_skill_mischief} 5"],
    f"{SkillNames.base_skill_mischief} 5": ["Menu", f"{SkillNames.base_skill_mischief} 6"],
    f"{SkillNames.base_skill_mischief} 6": ["Menu", f"{SkillNames.base_skill_mischief} 7"],
    f"{SkillNames.base_skill_mischief} 7": ["Menu", f"{SkillNames.base_skill_mischief} 8"],
    f"{SkillNames.base_skill_mischief} 8": ["Menu", f"{SkillNames.base_skill_mischief} 9"],
    f"{SkillNames.base_skill_mischief} 9": ["Menu", f"{SkillNames.base_skill_mischief} 10"],

    f"{SkillNames.base_skill_mixology} 1": ["Menu", f"{SkillNames.base_skill_mixology} 2"],
    f"{SkillNames.base_skill_mixology} 2": ["Menu", f"{SkillNames.base_skill_mixology} 3"],
    f"{SkillNames.base_skill_mixology} 3": ["Menu", f"{SkillNames.base_skill_mixology} 4"],
    f"{SkillNames.base_skill_mixology} 4": ["Menu", f"{SkillNames.base_skill_mixology} 5"],
    f"{SkillNames.base_skill_mixology} 5": ["Menu", f"{SkillNames.base_skill_mixology} 6"],
    f"{SkillNames.base_skill_mixology} 6": ["Menu", f"{SkillNames.base_skill_mixology} 7"],
    f"{SkillNames.base_skill_mixology} 7": ["Menu", f"{SkillNames.base_skill_mixology} 8"],
    f"{SkillNames.base_skill_mixology} 8": ["Menu", f"{SkillNames.base_skill_mixology} 9"],
    f"{SkillNames.base_skill_mixology} 9": ["Menu", f"{SkillNames.base_skill_mixology} 10"],

    f"{SkillNames.base_skill_cooking} 1": ["Menu", f"{SkillNames.base_skill_cooking} 2"],
    f"{SkillNames.base_skill_cooking} 2": ["Menu", f"{SkillNames.base_skill_cooking} 3"],
    f"{SkillNames.base_skill_cooking} 3": ["Menu", f"{SkillNames.base_skill_cooking} 4"],
    f"{SkillNames.base_skill_cooking} 4": ["Menu", f"{SkillNames.base_skill_cooking} 5"],
    f"{SkillNames.base_skill_cooking} 5": ["Menu", f"{SkillNames.base_skill_cooking} 6"],
    f"{SkillNames.base_skill_cooking} 6": ["Menu", f"{SkillNames.base_skill_cooking} 7",
                                           f"{SkillNames.base_skill_gourmet} 1"],
    f"{SkillNames.base_skill_cooking} 7": ["Menu", f"{SkillNames.base_skill_cooking} 8"],
    f"{SkillNames.base_skill_cooking} 8": ["Menu", f"{SkillNames.base_skill_cooking} 9"],
    f"{SkillNames.base_skill_cooking} 9": ["Menu", f"{SkillNames.base_skill_cooking} 10"],

    f"{SkillNames.base_skill_gourmet} 1": ["Menu", f"{SkillNames.base_skill_gourmet} 2"],
    f"{SkillNames.base_skill_gourmet} 2": ["Menu", f"{SkillNames.base_skill_gourmet} 3"],
    f"{SkillNames.base_skill_gourmet} 3": ["Menu", f"{SkillNames.base_skill_gourmet} 4"],
    f"{SkillNames.base_skill_gourmet} 4": ["Menu", f"{SkillNames.base_skill_gourmet} 5"],
    f"{SkillNames.base_skill_gourmet} 5": ["Menu", f"{SkillNames.base_skill_gourmet} 6"],
    f"{SkillNames.base_skill_gourmet} 6": ["Menu", f"{SkillNames.base_skill_gourmet} 7"],
    f"{SkillNames.base_skill_gourmet} 7": ["Menu", f"{SkillNames.base_skill_gourmet} 8"],
    f"{SkillNames.base_skill_gourmet} 8": ["Menu", f"{SkillNames.base_skill_gourmet} 9"],
    f"{SkillNames.base_skill_gourmet} 9": ["Menu", f"{SkillNames.base_skill_gourmet} 10"],

    f"{SkillNames.base_skill_rocket_science} 1": ["Menu", f"{SkillNames.base_skill_rocket_science} 2"],
    f"{SkillNames.base_skill_rocket_science} 2": ["Menu", f"{SkillNames.base_skill_rocket_science} 3"],
    f"{SkillNames.base_skill_rocket_science} 3": ["Menu", f"{SkillNames.base_skill_rocket_science} 4"],
    f"{SkillNames.base_skill_rocket_science} 4": ["Menu", f"{SkillNames.base_skill_rocket_science} 5"],
    f"{SkillNames.base_skill_rocket_science} 5": ["Menu", f"{SkillNames.base_skill_rocket_science} 6"],
    f"{SkillNames.base_skill_rocket_science} 6": ["Menu", f"{SkillNames.base_skill_rocket_science} 7"],
    f"{SkillNames.base_skill_rocket_science} 7": ["Menu", f"{SkillNames.base_skill_rocket_science} 8"],
    f"{SkillNames.base_skill_rocket_science} 8": ["Menu", f"{SkillNames.base_skill_rocket_science} 9"],
    f"{SkillNames.base_skill_rocket_science} 9": ["Menu", f"{SkillNames.base_skill_rocket_science} 10"],

    f"{SkillNames.base_skill_photography} 1": ["Menu", f"{SkillNames.base_skill_photography} 2"],
    f"{SkillNames.base_skill_photography} 2": ["Menu", f"{SkillNames.base_skill_photography} 3"],
    f"{SkillNames.base_skill_photography} 3": ["Menu", f"{SkillNames.base_skill_photography} 4"],
    f"{SkillNames.base_skill_photography} 4": ["Menu", f"{SkillNames.base_skill_photography} 5"],

    f"{SkillNames.base_skill_painting} 1": ["Menu", f"{SkillNames.base_skill_painting} 2"],
    f"{SkillNames.base_skill_painting} 2": ["Menu", f"{SkillNames.base_skill_painting} 3"],
    f"{SkillNames.base_skill_painting} 3": ["Menu", f"{SkillNames.base_skill_painting} 4"],
    f"{SkillNames.base_skill_painting} 4": ["Menu", f"{SkillNames.base_skill_painting} 5"],
    f"{SkillNames.base_skill_painting} 5": ["Menu", f"{SkillNames.base_skill_painting} 6"],
    f"{SkillNames.base_skill_painting} 6": ["Menu", f"{SkillNames.base_skill_painting} 7"],
    f"{SkillNames.base_skill_painting} 7": ["Menu", f"{SkillNames.base_skill_painting} 8"],
    f"{SkillNames.base_skill_painting} 8": ["Menu", f"{SkillNames.base_skill_painting} 9"],
    f"{SkillNames.base_skill_painting} 9": ["Menu", f"{SkillNames.base_skill_painting} 10"],

    f"{SkillNames.base_skill_guitar} 1": ["Menu", f"{SkillNames.base_skill_guitar} 2"],
    f"{SkillNames.base_skill_guitar} 2": ["Menu", f"{SkillNames.base_skill_guitar} 3"],
    f"{SkillNames.base_skill_guitar} 3": ["Menu", f"{SkillNames.base_skill_guitar} 4"],
    f"{SkillNames.base_skill_guitar} 4": ["Menu", f"{SkillNames.base_skill_guitar} 5"],
    f"{SkillNames.base_skill_guitar} 5": ["Menu", f"{SkillNames.base_skill_guitar} 6"],
    f"{SkillNames.base_skill_guitar} 6": ["Menu", f"{SkillNames.base_skill_guitar} 7"],
    f"{SkillNames.base_skill_guitar} 7": ["Menu", f"{SkillNames.base_skill_guitar} 8"],
    f"{SkillNames.base_skill_guitar} 8": ["Menu", f"{SkillNames.base_skill_guitar} 9"],
    f"{SkillNames.base_skill_guitar} 9": ["Menu", f"{SkillNames.base_skill_guitar} 10"],

    f"{SkillNames.base_skill_violin} 1": ["Menu", f"{SkillNames.base_skill_violin} 2"],
    f"{SkillNames.base_skill_violin} 2": ["Menu", f"{SkillNames.base_skill_violin} 3"],
    f"{SkillNames.base_skill_violin} 3": ["Menu", f"{SkillNames.base_skill_violin} 4"],
    f"{SkillNames.base_skill_violin} 4": ["Menu", f"{SkillNames.base_skill_violin} 5"],
    f"{SkillNames.base_skill_violin} 5": ["Menu", f"{SkillNames.base_skill_violin} 6"],
    f"{SkillNames.base_skill_violin} 6": ["Menu", f"{SkillNames.base_skill_violin} 7"],
    f"{SkillNames.base_skill_violin} 7": ["Menu", f"{SkillNames.base_skill_violin} 8"],
    f"{SkillNames.base_skill_violin} 8": ["Menu", f"{SkillNames.base_skill_violin} 9"],
    f"{SkillNames.base_skill_violin} 9": ["Menu", f"{SkillNames.base_skill_violin} 10"],

    f"{SkillNames.base_skill_piano} 1": ["Menu", f"{SkillNames.base_skill_piano} 2"],
    f"{SkillNames.base_skill_piano} 2": ["Menu", f"{SkillNames.base_skill_piano} 3"],
    f"{SkillNames.base_skill_piano} 3": ["Menu", f"{SkillNames.base_skill_piano} 4"],
    f"{SkillNames.base_skill_piano} 4": ["Menu", f"{SkillNames.base_skill_piano} 5"],
    f"{SkillNames.base_skill_piano} 5": ["Menu", f"{SkillNames.base_skill_piano} 6"],
    f"{SkillNames.base_skill_piano} 6": ["Menu", f"{SkillNames.base_skill_piano} 7"],
    f"{SkillNames.base_skill_piano} 7": ["Menu", f"{SkillNames.base_skill_piano} 8"],
    f"{SkillNames.base_skill_piano} 8": ["Menu", f"{SkillNames.base_skill_piano} 9"],
    f"{SkillNames.base_skill_piano} 9": ["Menu", f"{SkillNames.base_skill_piano} 10"],

    f"{SkillNames.base_skill_handiness} 1": ["Menu", f"{SkillNames.base_skill_handiness} 2"],
    f"{SkillNames.base_skill_handiness} 2": ["Menu", f"{SkillNames.base_skill_handiness} 3"],
    f"{SkillNames.base_skill_handiness} 3": ["Menu", f"{SkillNames.base_skill_handiness} 4"],
    f"{SkillNames.base_skill_handiness} 4": ["Menu", f"{SkillNames.base_skill_handiness} 5"],
    f"{SkillNames.base_skill_handiness} 5": ["Menu", f"{SkillNames.base_skill_handiness} 6"],
    f"{SkillNames.base_skill_handiness} 6": ["Menu", f"{SkillNames.base_skill_handiness} 7"],
    f"{SkillNames.base_skill_handiness} 7": ["Menu", f"{SkillNames.base_skill_handiness} 8"],
    f"{SkillNames.base_skill_handiness} 8": ["Menu", f"{SkillNames.base_skill_handiness} 9"],
    f"{SkillNames.base_skill_handiness} 9": ["Menu", f"{SkillNames.base_skill_handiness} 10"],

    f"{SkillNames.base_skill_programming} 1": ["Menu", f"{SkillNames.base_skill_programming} 2"],
    f"{SkillNames.base_skill_programming} 2": ["Menu", f"{SkillNames.base_skill_programming} 3"],
    f"{SkillNames.base_skill_programming} 3": ["Menu", f"{SkillNames.base_skill_programming} 4"],
    f"{SkillNames.base_skill_programming} 4": ["Menu", f"{SkillNames.base_skill_programming} 5"],
    f"{SkillNames.base_skill_programming} 5": ["Menu", f"{SkillNames.base_skill_programming} 6"],
    f"{SkillNames.base_skill_programming} 6": ["Menu", f"{SkillNames.base_skill_programming} 7"],
    f"{SkillNames.base_skill_programming} 7": ["Menu", f"{SkillNames.base_skill_programming} 8"],
    f"{SkillNames.base_skill_programming} 8": ["Menu", f"{SkillNames.base_skill_programming} 9"],
    f"{SkillNames.base_skill_programming} 9": ["Menu", f"{SkillNames.base_skill_programming} 10"],

    f"{SkillNames.base_skill_video_gaming} 1": ["Menu", f"{SkillNames.base_skill_video_gaming} 2"],
    f"{SkillNames.base_skill_video_gaming} 2": ["Menu", f"{SkillNames.base_skill_video_gaming} 3"],
    f"{SkillNames.base_skill_video_gaming} 3": ["Menu", f"{SkillNames.base_skill_video_gaming} 4"],
    f"{SkillNames.base_skill_video_gaming} 4": ["Menu", f"{SkillNames.base_skill_video_gaming} 5"],
    f"{SkillNames.base_skill_video_gaming} 5": ["Menu", f"{SkillNames.base_skill_video_gaming} 6"],
    f"{SkillNames.base_skill_video_gaming} 6": ["Menu", f"{SkillNames.base_skill_video_gaming} 7"],
    f"{SkillNames.base_skill_video_gaming} 7": ["Menu", f"{SkillNames.base_skill_video_gaming} 8"],
    f"{SkillNames.base_skill_video_gaming} 8": ["Menu", f"{SkillNames.base_skill_video_gaming} 9"],
    f"{SkillNames.base_skill_video_gaming} 9": ["Menu", f"{SkillNames.base_skill_video_gaming} 10"],

    f"{SkillNames.base_skill_gardening} 1": ["Menu", f"{SkillNames.base_skill_gardening} 2"],
    f"{SkillNames.base_skill_gardening} 2": ["Menu", f"{SkillNames.base_skill_gardening} 3"],
    f"{SkillNames.base_skill_gardening} 3": ["Menu", f"{SkillNames.base_skill_gardening} 4"],
    f"{SkillNames.base_skill_gardening} 4": ["Menu", f"{SkillNames.base_skill_gardening} 5"],
    f"{SkillNames.base_skill_gardening} 5": ["Menu", f"{SkillNames.base_skill_gardening} 6"],
    f"{SkillNames.base_skill_gardening} 6": ["Menu", f"{SkillNames.base_skill_gardening} 7"],
    f"{SkillNames.base_skill_gardening} 7": ["Menu", f"{SkillNames.base_skill_gardening} 8"],
    f"{SkillNames.base_skill_gardening} 8": ["Menu", f"{SkillNames.base_skill_gardening} 9"],
    f"{SkillNames.base_skill_gardening} 9": ["Menu", f"{SkillNames.base_skill_gardening} 10"],

    f"{SkillNames.base_skill_fishing} 1": ["Menu", f"{SkillNames.base_skill_fishing} 2"],
    f"{SkillNames.base_skill_fishing} 2": ["Menu", f"{SkillNames.base_skill_fishing} 3"],
    f"{SkillNames.base_skill_fishing} 3": ["Menu", f"{SkillNames.base_skill_fishing} 4"],
    f"{SkillNames.base_skill_fishing} 4": ["Menu", f"{SkillNames.base_skill_fishing} 5"],
    f"{SkillNames.base_skill_fishing} 5": ["Menu", f"{SkillNames.base_skill_fishing} 6"],
    f"{SkillNames.base_skill_fishing} 6": ["Menu", f"{SkillNames.base_skill_fishing} 7"],
    f"{SkillNames.base_skill_fishing} 7": ["Menu", f"{SkillNames.base_skill_fishing} 8"],
    f"{SkillNames.base_skill_fishing} 8": ["Menu", f"{SkillNames.base_skill_fishing} 9"],
    f"{SkillNames.base_skill_fishing} 9": ["Menu", f"{SkillNames.base_skill_fishing} 10"],

    f"{SkillNames.base_skill_writing} 1": ["Menu", f"{SkillNames.base_skill_writing} 2"],
    f"{SkillNames.base_skill_writing} 2": ["Menu", f"{SkillNames.base_skill_writing} 3"],
    f"{SkillNames.base_skill_writing} 3": ["Menu", f"{SkillNames.base_skill_writing} 4"],
    f"{SkillNames.base_skill_writing} 4": ["Menu", f"{SkillNames.base_skill_writing} 5"],
    f"{SkillNames.base_skill_writing} 5": ["Menu", f"{SkillNames.base_skill_writing} 6"],
    f"{SkillNames.base_skill_writing} 6": ["Menu", f"{SkillNames.base_skill_writing} 7"],
    f"{SkillNames.base_skill_writing} 7": ["Menu", f"{SkillNames.base_skill_writing} 8"],
    f"{SkillNames.base_skill_writing} 8": ["Menu", f"{SkillNames.base_skill_writing} 9"],
    f"{SkillNames.base_skill_writing} 9": ["Menu", f"{SkillNames.base_skill_writing} 10"],

    f"{SkillNames.base_skill_comedy} 1": ["Menu", f"{SkillNames.base_skill_comedy} 2"],
    f"{SkillNames.base_skill_comedy} 2": ["Menu", f"{SkillNames.base_skill_comedy} 3"],
    f"{SkillNames.base_skill_comedy} 3": ["Menu", f"{SkillNames.base_skill_comedy} 4"],
    f"{SkillNames.base_skill_comedy} 4": ["Menu", f"{SkillNames.base_skill_comedy} 5"],
    f"{SkillNames.base_skill_comedy} 5": ["Menu", f"{SkillNames.base_skill_comedy} 6"],
    f"{SkillNames.base_skill_comedy} 6": ["Menu", f"{SkillNames.base_skill_comedy} 7"],
    f"{SkillNames.base_skill_comedy} 7": ["Menu", f"{SkillNames.base_skill_comedy} 8"],
    f"{SkillNames.base_skill_comedy} 8": ["Menu", f"{SkillNames.base_skill_comedy} 9"],
    f"{SkillNames.base_skill_comedy} 9": ["Menu", f"{SkillNames.base_skill_comedy} 10"],
}
