# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll11l1_opy_ import bstack1ll1ll11111_opy_
from browserstack_sdk.sdk_cli.utils.bstack11ll1111l_opy_ import bstack1ll11l1l1l1_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l111l1_opy_,
    bstack1lll1l1l1ll_opy_,
    bstack1lll1ll1ll1_opy_,
    bstack1ll1l111lll_opy_,
    bstack1l1llll111l_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l1l11l1_opy_
from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll11l11l1l_opy_ import bstack1ll11llll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll111llll_opy_ import bstack1lll11l111l_opy_
bstack1ll111l1l1l_opy_ = bstack1ll1l1l11l1_opy_()
bstack1l1lll1l1l1_opy_ = bstack11ll1ll_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧር")
bstack1ll11l1llll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤሮ")
bstack1ll111ll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨሯ")
bstack1l1lll1ll11_opy_ = 1.0
_1ll1l1l1l11_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll111lll1l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣሰ")
    bstack1ll11l1111l_opy_ = bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࠢሱ")
    bstack1ll111llll1_opy_ = bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤሲ")
    bstack1l1lllll11l_opy_ = bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࠨሳ")
    bstack1l1llllll11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣሴ")
    bstack1l1lll1ll1l_opy_: bool
    bstack1lll111llll_opy_: bstack1lll11l111l_opy_  = None
    bstack1ll1l1l1l1l_opy_ = [
        bstack1lll1l111l1_opy_.BEFORE_ALL,
        bstack1lll1l111l1_opy_.AFTER_ALL,
        bstack1lll1l111l1_opy_.BEFORE_EACH,
        bstack1lll1l111l1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11ll1l11_opy_: Dict[str, str],
        bstack1ll1l11111l_opy_: List[str]=[bstack11ll1ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥስ")],
        bstack1lll111llll_opy_: bstack1lll11l111l_opy_ = None,
        bstack1llllll1l1l_opy_=None
    ):
        super().__init__(bstack1ll1l11111l_opy_, bstack1ll11ll1l11_opy_, bstack1lll111llll_opy_)
        self.bstack1l1lll1ll1l_opy_ = any(bstack11ll1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦሶ") in item.lower() for item in bstack1ll1l11111l_opy_)
        self.bstack1llllll1l1l_opy_ = bstack1llllll1l1l_opy_
    def track_event(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l111l1_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1l1l1l1l_opy_:
            bstack1ll11l1l1l1_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l111l1_opy_.NONE:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࠤሷ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠤࠥሸ"))
            return
        if not self.bstack1l1lll1ll1l_opy_:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡀࠦሹ") + str(str(self.bstack1ll1l11111l_opy_)) + bstack11ll1ll_opy_ (u"ࠦࠧሺ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሻ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠨࠢሼ"))
            return
        instance = self.__1ll111l1lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡢࡴࡪࡷࡂࠨሽ") + str(args) + bstack11ll1ll_opy_ (u"ࠣࠤሾ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1l1l1l_opy_ and test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack11lll1l1ll_opy_.value)
                name = str(EVENTS.bstack11lll1l1ll_opy_.name)+bstack11ll1ll_opy_ (u"ࠤ࠽ࠦሿ")+str(test_framework_state.name)
                TestFramework.bstack1ll11ll11ll_opy_(instance, name, bstack1l1lll1l1ll_opy_)
        except Exception as e:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࠦࡰࡳࡧ࠽ࠤࢀࢃࠢቀ").format(e))
        try:
            if test_framework_state == bstack1lll1l111l1_opy_.TEST:
                if not TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1ll1l11llll_opy_) and test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1111ll1l_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡱࡵࡡࡥࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦቁ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠧࠨቂ"))
                if test_hook_state == bstack1lll1ll1ll1_opy_.PRE and not TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1ll1l11ll1l_opy_):
                    TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l11ll1l_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11lll1l1_opy_(instance, args)
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡵࡷࡥࡷࡺࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦቃ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠢࠣቄ"))
                elif test_hook_state == bstack1lll1ll1ll1_opy_.POST and not TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_):
                    TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡩࡳࡪࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦቅ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠤࠥቆ"))
            elif test_framework_state == bstack1lll1l111l1_opy_.STEP:
                if test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                    PytestBDDFramework.__1ll1l11l111_opy_(instance, args)
                elif test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                    PytestBDDFramework.__1ll1111l1ll_opy_(instance, args)
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG and test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                PytestBDDFramework.__1ll111111ll_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG_REPORT and test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                self.__1ll1l11l1ll_opy_(instance, *args)
                self.__1ll111111l1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1l1l1l1l_opy_:
                self.__1ll111ll111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦቇ") + str(instance.ref()) + bstack11ll1ll_opy_ (u"ࠦࠧቈ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11l1lll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1l1l1l_opy_ and test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                name = str(EVENTS.bstack11lll1l1ll_opy_.name)+bstack11ll1ll_opy_ (u"ࠧࡀࠢ቉")+str(test_framework_state.name)
                bstack1l1lll1l1ll_opy_ = TestFramework.bstack1ll11lllll1_opy_(instance, name)
                bstack1llll11l11l_opy_.end(EVENTS.bstack11lll1l1ll_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨቊ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧቋ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣቌ").format(e))
    def bstack1l1lllll111_opy_(self):
        return self.bstack1l1lll1ll1l_opy_
    def __1ll11111l11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11ll1ll_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨቍ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1llll1lll_opy_(rep, [bstack11ll1ll_opy_ (u"ࠥࡻ࡭࡫࡮ࠣ቎"), bstack11ll1ll_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧ቏"), bstack11ll1ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧቐ"), bstack11ll1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨቑ"), bstack11ll1ll_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠣቒ"), bstack11ll1ll_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢቓ")])
        return None
    def __1ll1l11l1ll_opy_(self, instance: bstack1lll1l1l1ll_opy_, *args):
        result = self.__1ll11111l11_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111l11_opy_ = None
        if result.get(bstack11ll1ll_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥቔ"), None) == bstack11ll1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥቕ") and len(args) > 1 and getattr(args[1], bstack11ll1ll_opy_ (u"ࠦࡪࡾࡣࡪࡰࡩࡳࠧቖ"), None) is not None:
            failure = [{bstack11ll1ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ቗"): [args[1].excinfo.exconly(), result.get(bstack11ll1ll_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧቘ"), None)]}]
            bstack1111111l11_opy_ = bstack11ll1ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ቙") if bstack11ll1ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦቚ") in getattr(args[1].excinfo, bstack11ll1ll_opy_ (u"ࠤࡷࡽࡵ࡫࡮ࡢ࡯ࡨࠦቛ"), bstack11ll1ll_opy_ (u"ࠥࠦቜ")) else bstack11ll1ll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧቝ")
        bstack1l1lll1l11l_opy_ = result.get(bstack11ll1ll_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨ቞"), TestFramework.bstack1l1lll1lll1_opy_)
        if bstack1l1lll1l11l_opy_ != TestFramework.bstack1l1lll1lll1_opy_:
            TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1l1lll1llll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11ll1l1l_opy_(instance, {
            TestFramework.bstack1lll1l1111l_opy_: failure,
            TestFramework.bstack1ll1l11l1l1_opy_: bstack1111111l11_opy_,
            TestFramework.bstack1llll1111l1_opy_: bstack1l1lll1l11l_opy_,
        })
    def __1ll111l1lll_opy_(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l111l1_opy_.SETUP_FIXTURE:
            instance = self.__1ll11l1l11l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1111lll1_opy_ bstack1ll1l1111l1_opy_ this to be bstack11ll1ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨ቟")
            if test_framework_state == bstack1lll1l111l1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1llllllll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11ll1ll_opy_ (u"ࠢ࡯ࡱࡧࡩࠧበ"), None), bstack11ll1ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣቡ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11ll1ll_opy_ (u"ࠤࡱࡳࡩ࡫ࠢቢ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11ll1ll_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥባ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11l1ll11_opy_(target) if target else None
        return instance
    def __1ll111ll111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll111l1ll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l1111l_opy_, {})
        if not key in bstack1ll111l1ll1_opy_:
            bstack1ll111l1ll1_opy_[key] = []
        bstack1ll11l11ll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111llll1_opy_, {})
        if not key in bstack1ll11l11ll1_opy_:
            bstack1ll11l11ll1_opy_[key] = []
        bstack1ll1l1l1111_opy_ = {
            PytestBDDFramework.bstack1ll11l1111l_opy_: bstack1ll111l1ll1_opy_,
            PytestBDDFramework.bstack1ll111llll1_opy_: bstack1ll11l11ll1_opy_,
        }
        if test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11ll1ll_opy_ (u"ࠦࡰ࡫ࡹࠣቤ"): key,
                TestFramework.bstack1ll1l11l11l_opy_: uuid4().__str__(),
                TestFramework.bstack1l1llll1l1l_opy_: TestFramework.bstack1ll1111l11l_opy_,
                TestFramework.bstack1l1lllll1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1l111_opy_: [],
                TestFramework.bstack1ll11111111_opy_: hook_name,
                TestFramework.bstack1ll1l111l1l_opy_: bstack1ll11llll11_opy_.bstack1ll11llll1l_opy_()
            }
            bstack1ll111l1ll1_opy_[key].append(hook)
            bstack1ll1l1l1111_opy_[PytestBDDFramework.bstack1l1lllll11l_opy_] = key
        elif test_hook_state == bstack1lll1ll1ll1_opy_.POST:
            bstack1l1llll1ll1_opy_ = bstack1ll111l1ll1_opy_.get(key, [])
            hook = bstack1l1llll1ll1_opy_.pop() if bstack1l1llll1ll1_opy_ else None
            if hook:
                result = self.__1ll11111l11_opy_(*args)
                if result:
                    bstack1ll11lll111_opy_ = result.get(bstack11ll1ll_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨብ"), TestFramework.bstack1ll1111l11l_opy_)
                    if bstack1ll11lll111_opy_ != TestFramework.bstack1ll1111l11l_opy_:
                        hook[TestFramework.bstack1l1llll1l1l_opy_] = bstack1ll11lll111_opy_
                hook[TestFramework.bstack1ll1l111ll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l111l1l_opy_] = bstack1ll11llll11_opy_.bstack1ll11llll1l_opy_()
                self.bstack1ll11111ll1_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1111ll11_opy_, [])
                self.bstack1ll1111l111_opy_(instance, logs)
                bstack1ll11l11ll1_opy_[key].append(hook)
                bstack1ll1l1l1111_opy_[PytestBDDFramework.bstack1l1llllll11_opy_] = key
        TestFramework.bstack1ll11ll1l1l_opy_(instance, bstack1ll1l1l1111_opy_)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡮࡯ࡰ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁ࡫ࡦࡻࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤ࠾ࡽ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡁࠧቦ") + str(bstack1ll11l11ll1_opy_) + bstack11ll1ll_opy_ (u"ࠢࠣቧ"))
    def __1ll11l1l11l_opy_(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1llll1lll_opy_(args[0], [bstack11ll1ll_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢቨ"), bstack11ll1ll_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥቩ"), bstack11ll1ll_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥቪ"), bstack11ll1ll_opy_ (u"ࠦ࡮ࡪࡳࠣቫ"), bstack11ll1ll_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢቬ"), bstack11ll1ll_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨቭ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11ll1ll_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨቮ")) else fixturedef.get(bstack11ll1ll_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢቯ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11ll1ll_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢተ")) else None
        node = request.node if hasattr(request, bstack11ll1ll_opy_ (u"ࠥࡲࡴࡪࡥࠣቱ")) else None
        target = request.node.nodeid if hasattr(node, bstack11ll1ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦቲ")) else None
        baseid = fixturedef.get(bstack11ll1ll_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧታ"), None) or bstack11ll1ll_opy_ (u"ࠨࠢቴ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11ll1ll_opy_ (u"ࠢࡠࡲࡼࡪࡺࡴࡣࡪࡶࡨࡱࠧት")):
            target = PytestBDDFramework.__1ll11ll111l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11ll1ll_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥቶ")) else None
            if target and not TestFramework.bstack1ll11l1ll11_opy_(target):
                self.__1l1llllllll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡳࡵࡤࡦ࠿ࡾࡲࡴࡪࡥࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦቷ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠥࠦቸ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤቹ") + str(target) + bstack11ll1ll_opy_ (u"ࠧࠨቺ"))
            return None
        instance = TestFramework.bstack1ll11l1ll11_opy_(target)
        if not instance:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡨࡡࡴࡧ࡬ࡨࡂࢁࡢࡢࡵࡨ࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣቻ") + str(target) + bstack11ll1ll_opy_ (u"ࠢࠣቼ"))
            return None
        bstack1l1lllllll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111lll1l_opy_, {})
        if os.getenv(bstack11ll1ll_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡇࡋ࡛ࡘ࡚ࡘࡅࡔࠤች"), bstack11ll1ll_opy_ (u"ࠤ࠴ࠦቾ")) == bstack11ll1ll_opy_ (u"ࠥ࠵ࠧቿ"):
            bstack1ll11l1ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠦ࠿ࠨኀ").join((scope, fixturename))
            bstack1ll11l11lll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l111l11_opy_ = {
                bstack11ll1ll_opy_ (u"ࠧࡱࡥࡺࠤኁ"): bstack1ll11l1ll1l_opy_,
                bstack11ll1ll_opy_ (u"ࠨࡴࡢࡩࡶࠦኂ"): PytestBDDFramework.__1ll1l1111ll_opy_(request.node, scenario),
                bstack11ll1ll_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࠣኃ"): fixturedef,
                bstack11ll1ll_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢኄ"): scope,
                bstack11ll1ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢኅ"): None,
            }
            try:
                if test_hook_state == bstack1lll1ll1ll1_opy_.POST and callable(getattr(args[-1], bstack11ll1ll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢኆ"), None)):
                    bstack1ll1l111l11_opy_[bstack11ll1ll_opy_ (u"ࠦࡹࡿࡰࡦࠤኇ")] = TestFramework.bstack1ll1l11lll1_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                bstack1ll1l111l11_opy_[bstack11ll1ll_opy_ (u"ࠧࡻࡵࡪࡦࠥኈ")] = uuid4().__str__()
                bstack1ll1l111l11_opy_[PytestBDDFramework.bstack1l1lllll1l1_opy_] = bstack1ll11l11lll_opy_
            elif test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                bstack1ll1l111l11_opy_[PytestBDDFramework.bstack1ll1l111ll1_opy_] = bstack1ll11l11lll_opy_
            if bstack1ll11l1ll1l_opy_ in bstack1l1lllllll1_opy_:
                bstack1l1lllllll1_opy_[bstack1ll11l1ll1l_opy_].update(bstack1ll1l111l11_opy_)
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࠢ኉") + str(bstack1l1lllllll1_opy_[bstack1ll11l1ll1l_opy_]) + bstack11ll1ll_opy_ (u"ࠢࠣኊ"))
            else:
                bstack1l1lllllll1_opy_[bstack1ll11l1ll1l_opy_] = bstack1ll1l111l11_opy_
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࢃࠠࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࠦኋ") + str(len(bstack1l1lllllll1_opy_)) + bstack11ll1ll_opy_ (u"ࠤࠥኌ"))
        TestFramework.bstack1lllllll1l1_opy_(instance, PytestBDDFramework.bstack1ll111lll1l_opy_, bstack1l1lllllll1_opy_)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࢀࡲࡥ࡯ࠪࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷ࠮ࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥኍ") + str(instance.ref()) + bstack11ll1ll_opy_ (u"ࠦࠧ኎"))
        return instance
    def __1l1llllllll_opy_(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        ob = bstack1lll1l1l1ll_opy_(ctx, self.bstack1ll1l11111l_opy_, self.bstack1ll11ll1l11_opy_, test_framework_state)
        TestFramework.bstack1ll11ll1l1l_opy_(ob, {
            TestFramework.bstack1lll1ll11ll_opy_: context.test_framework_name,
            TestFramework.bstack1lll11ll1ll_opy_: context.test_framework_version,
            TestFramework.bstack1ll111l1111_opy_: [],
            PytestBDDFramework.bstack1ll111lll1l_opy_: {},
            PytestBDDFramework.bstack1ll111llll1_opy_: {},
            PytestBDDFramework.bstack1ll11l1111l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllllll1l1_opy_(ob, TestFramework.bstack1l1llll11l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllllll1l1_opy_(ob, TestFramework.bstack1llll1l11ll_opy_, context.platform_index)
        TestFramework.bstack1llll111111_opy_[ctx.id] = ob
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡣࡵࡺ࠱࡭ࡩࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧ኏") + str(TestFramework.bstack1llll111111_opy_.keys()) + bstack11ll1ll_opy_ (u"ࠨࠢነ"))
        return ob
    @staticmethod
    def __1ll11lll1l1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll1ll_opy_ (u"ࠧࡪࡦࠪኑ"): id(step),
                bstack11ll1ll_opy_ (u"ࠨࡶࡨࡼࡹ࠭ኒ"): step.name,
                bstack11ll1ll_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪና"): step.keyword,
            })
        meta = {
            bstack11ll1ll_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫኔ"): {
                bstack11ll1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩን"): feature.name,
                bstack11ll1ll_opy_ (u"ࠬࡶࡡࡵࡪࠪኖ"): feature.filename,
                bstack11ll1ll_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫኗ"): feature.description
            },
            bstack11ll1ll_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩኘ"): {
                bstack11ll1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ኙ"): scenario.name
            },
            bstack11ll1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኚ"): steps,
            bstack11ll1ll_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬኛ"): PytestBDDFramework.__1ll1111111l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll111ll1ll_opy_: meta
            }
        )
    def bstack1ll11111ll1_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡶ࡭ࡲ࡯࡬ࡢࡴࠣࡸࡴࠦࡴࡩࡧࠣࡎࡦࡼࡡࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡅ࡫ࡩࡨࡱࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡮ࡴࡳࡪࡦࡨࠤࢃ࠵࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠵ࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠯ࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡸࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨࠠࡪࡰࠣ࡭ࡹࡹࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡎ࡬ࠠࡢࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣࡸ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡱࡦࡺࡣࡩࡧࡶࠤࡦࠦ࡭ࡰࡦ࡬ࡪ࡮࡫ࡤࠡࡪࡲࡳࡰ࠳࡬ࡦࡸࡨࡰࠥ࡬ࡩ࡭ࡧ࠯ࠤ࡮ࡺࠠࡤࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࠥࡽࡩࡵࡪࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡔ࡫ࡰ࡭ࡱࡧࡲ࡭ࡻ࠯ࠤ࡮ࡺࠠࡱࡴࡲࡧࡪࡹࡳࡦࡵࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡲ࡯ࡤࡣࡷࡩࡩࠦࡩ࡯ࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡧࡿࠠࡳࡧࡳࡰࡦࡩࡩ࡯ࡩࠣࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡘ࡭࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࡶࠤࡦࡸࡥࠡࡣࡧࡨࡪࡪࠠࡵࡱࠣࡸ࡭࡫ࠠࡩࡱࡲ࡯ࠬࡹࠠࠣ࡮ࡲ࡫ࡸࠨࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬࠼ࠣࡘ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹࠠࡢࡰࡧࠤ࡭ࡵ࡯࡬ࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩ࡚ࠥࡥࡴࡶࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኜ")
        global _1ll1l1l1l11_opy_
        platform_index = os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬኝ")]
        bstack1ll1111llll_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1l1lll1l1l1_opy_ + str(platform_index)), bstack1ll11l1llll_opy_)
        if not os.path.exists(bstack1ll1111llll_opy_) or not os.path.isdir(bstack1ll1111llll_opy_):
            return
        logs = hook.get(bstack11ll1ll_opy_ (u"ࠨ࡬ࡰࡩࡶࠦኞ"), [])
        with os.scandir(bstack1ll1111llll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l1l1l11_opy_:
                    self.logger.info(bstack11ll1ll_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧኟ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11ll1ll_opy_ (u"ࠣࠤአ")
                    log_entry = bstack1l1llll111l_opy_(
                        kind=bstack11ll1ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦኡ"),
                        message=bstack11ll1ll_opy_ (u"ࠥࠦኢ"),
                        level=bstack11ll1ll_opy_ (u"ࠦࠧኣ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1llllll1l_opy_=entry.stat().st_size,
                        bstack1ll111l11l1_opy_=bstack11ll1ll_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧኤ"),
                        bstack1111lll_opy_=os.path.abspath(entry.path),
                        bstack1ll11l1l1ll_opy_=hook.get(TestFramework.bstack1ll1l11l11l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l1l1l11_opy_.add(abs_path)
        platform_index = os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭እ")]
        bstack1ll11l111l1_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1l1lll1l1l1_opy_ + str(platform_index)), bstack1ll11l1llll_opy_, bstack1ll111ll1l1_opy_)
        if not os.path.exists(bstack1ll11l111l1_opy_) or not os.path.isdir(bstack1ll11l111l1_opy_):
            self.logger.info(bstack11ll1ll_opy_ (u"ࠢࡏࡱࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡪࡴࡻ࡮ࡥࠢࡤࡸ࠿ࠦࡻࡾࠤኦ").format(bstack1ll11l111l1_opy_))
        else:
            self.logger.info(bstack11ll1ll_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡩࡶࡴࡳࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠽ࠤࢀࢃࠢኧ").format(bstack1ll11l111l1_opy_))
            with os.scandir(bstack1ll11l111l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l1l1l11_opy_:
                        self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢከ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11ll1ll_opy_ (u"ࠥࠦኩ")
                        log_entry = bstack1l1llll111l_opy_(
                            kind=bstack11ll1ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨኪ"),
                            message=bstack11ll1ll_opy_ (u"ࠧࠨካ"),
                            level=bstack11ll1ll_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥኬ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1llllll1l_opy_=entry.stat().st_size,
                            bstack1ll111l11l1_opy_=bstack11ll1ll_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢክ"),
                            bstack1111lll_opy_=os.path.abspath(entry.path),
                            bstack1ll1l11ll11_opy_=hook.get(TestFramework.bstack1ll1l11l11l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l1l1l11_opy_.add(abs_path)
        hook[bstack11ll1ll_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨኮ")] = logs
    def bstack1ll1111l111_opy_(
        self,
        bstack1ll111l1l11_opy_: bstack1lll1l1l1ll_opy_,
        entries: List[bstack1l1llll111l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨኯ"))
        req.platform_index = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1llll1l11ll_opy_)
        req.execution_context.hash = str(bstack1ll111l1l11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111l1l11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111l1l11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll1ll11ll_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll11ll1ll_opy_)
            log_entry.uuid = entry.bstack1ll11l1l1ll_opy_ if entry.bstack1ll11l1l1ll_opy_ else TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll11llll1_opy_)
            log_entry.test_framework_state = bstack1ll111l1l11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11ll1ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤኰ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11ll1ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨ኱"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llllll1l_opy_
                log_entry.file_path = entry.bstack1111lll_opy_
        def bstack1l1lll11lll_opy_():
            bstack111111ll11_opy_ = datetime.now()
            try:
                self.bstack1llllll1l1l_opy_.LogCreatedEvent(req)
                bstack1ll111l1l11_opy_.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤኲ"), datetime.now() - bstack111111ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll1ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡾࢁࠧኳ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll111llll_opy_.enqueue(bstack1l1lll11lll_opy_)
    def __1ll111111l1_opy_(self, instance) -> None:
        bstack11ll1ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡑࡵࡡࡥࡵࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡦ࡭ࡳࠡࡨࡲࡶࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡳࡧࡤࡸࡪࡹࠠࡢࠢࡧ࡭ࡨࡺࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡹ࡫ࡳࡵࠢ࡯ࡩࡻ࡫࡬ࠡࡥࡸࡷࡹࡵ࡭ࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡦࡳࡱࡰࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡵࡴࡶࡲࡱ࡙ࡧࡧࡎࡣࡱࡥ࡬࡫ࡲࠡࡣࡱࡨࠥࡻࡰࡥࡣࡷࡩࡸࠦࡴࡩࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡹࡴࡢࡶࡨࠤࡺࡹࡩ࡯ࡩࠣࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧኴ")
        bstack1ll1l1l1111_opy_ = {bstack11ll1ll_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠥኵ"): bstack1ll11llll11_opy_.bstack1ll11llll1l_opy_()}
        TestFramework.bstack1ll11ll1l1l_opy_(instance, bstack1ll1l1l1111_opy_)
    @staticmethod
    def __1ll1l11l111_opy_(instance, args):
        request, bstack1ll111lllll_opy_ = args
        bstack1ll11ll1ll1_opy_ = id(bstack1ll111lllll_opy_)
        bstack1ll1l111111_opy_ = instance.data[TestFramework.bstack1ll111ll1ll_opy_]
        step = next(filter(lambda st: st[bstack11ll1ll_opy_ (u"ࠩ࡬ࡨࠬ኶")] == bstack1ll11ll1ll1_opy_, bstack1ll1l111111_opy_[bstack11ll1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ኷")]), None)
        step.update({
            bstack11ll1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨኸ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll1l111111_opy_[bstack11ll1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኹ")]) if st[bstack11ll1ll_opy_ (u"࠭ࡩࡥࠩኺ")] == step[bstack11ll1ll_opy_ (u"ࠧࡪࡦࠪኻ")]), None)
        if index is not None:
            bstack1ll1l111111_opy_[bstack11ll1ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኼ")][index] = step
        instance.data[TestFramework.bstack1ll111ll1ll_opy_] = bstack1ll1l111111_opy_
    @staticmethod
    def __1ll1111l1ll_opy_(instance, args):
        bstack11ll1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡷࡩࡧࡱࠤࡱ࡫࡮ࠡࡣࡵ࡫ࡸࠦࡩࡴࠢ࠵࠰ࠥ࡯ࡴࠡࡵ࡬࡫ࡳ࡯ࡦࡪࡧࡶࠤࡹ࡮ࡥࡳࡧࠣ࡭ࡸࠦ࡮ࡰࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡥࡷ࡭ࡳࠡࡣࡵࡩࠥ࠳ࠠ࡜ࡴࡨࡵࡺ࡫ࡳࡵ࠮ࠣࡷࡹ࡫ࡰ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡡࡳࡩࡶࠤࡦࡸࡥࠡ࠵ࠣࡸ࡭࡫࡮ࠡࡶ࡫ࡩࠥࡲࡡࡴࡶࠣࡺࡦࡲࡵࡦࠢ࡬ࡷࠥ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧኽ")
        bstack1ll11ll1lll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll111lllll_opy_ = args[1]
        bstack1ll11ll1ll1_opy_ = id(bstack1ll111lllll_opy_)
        bstack1ll1l111111_opy_ = instance.data[TestFramework.bstack1ll111ll1ll_opy_]
        step = None
        if bstack1ll11ll1ll1_opy_ is not None and bstack1ll1l111111_opy_.get(bstack11ll1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኾ")):
            step = next(filter(lambda st: st[bstack11ll1ll_opy_ (u"ࠫ࡮ࡪࠧ኿")] == bstack1ll11ll1ll1_opy_, bstack1ll1l111111_opy_[bstack11ll1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫዀ")]), None)
            step.update({
                bstack11ll1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ዁"): bstack1ll11ll1lll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11ll1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧዂ"): bstack11ll1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨዃ"),
                bstack11ll1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪዄ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11ll1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪዅ"): bstack11ll1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ዆"),
                })
        index = next((i for i, st in enumerate(bstack1ll1l111111_opy_[bstack11ll1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ዇")]) if st[bstack11ll1ll_opy_ (u"࠭ࡩࡥࠩወ")] == step[bstack11ll1ll_opy_ (u"ࠧࡪࡦࠪዉ")]), None)
        if index is not None:
            bstack1ll1l111111_opy_[bstack11ll1ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧዊ")][index] = step
        instance.data[TestFramework.bstack1ll111ll1ll_opy_] = bstack1ll1l111111_opy_
    @staticmethod
    def __1ll1111111l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11ll1ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫዋ")):
                examples = list(node.callspec.params[bstack11ll1ll_opy_ (u"ࠪࡣࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡧࡻࡥࡲࡶ࡬ࡦࠩዌ")].values())
            return examples
        except:
            return []
    def bstack1ll11l111ll_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_]):
        bstack1ll11l11111_opy_ = (
            PytestBDDFramework.bstack1l1lllll11l_opy_
            if bstack1lllllllll1_opy_[1] == bstack1lll1ll1ll1_opy_.PRE
            else PytestBDDFramework.bstack1l1llllll11_opy_
        )
        hook = PytestBDDFramework.bstack1ll11lll11l_opy_(instance, bstack1ll11l11111_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1l111_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll111l1111_opy_, []))
        return entries
    def bstack1ll11lll1ll_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_]):
        bstack1ll11l11111_opy_ = (
            PytestBDDFramework.bstack1l1lllll11l_opy_
            if bstack1lllllllll1_opy_[1] == bstack1lll1ll1ll1_opy_.PRE
            else PytestBDDFramework.bstack1l1llllll11_opy_
        )
        PytestBDDFramework.bstack1ll11ll1111_opy_(instance, bstack1ll11l11111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll111l1111_opy_, []).clear()
    @staticmethod
    def bstack1ll11lll11l_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll11l11111_opy_: str):
        bstack1l1llll1l11_opy_ = (
            PytestBDDFramework.bstack1ll111llll1_opy_
            if bstack1ll11l11111_opy_ == PytestBDDFramework.bstack1l1llllll11_opy_
            else PytestBDDFramework.bstack1ll11l1111l_opy_
        )
        bstack1ll11111l1l_opy_ = TestFramework.get_state(instance, bstack1ll11l11111_opy_, None)
        bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1l1llll1l11_opy_, None) if bstack1ll11111l1l_opy_ else None
        return (
            bstack1ll11llllll_opy_[bstack1ll11111l1l_opy_][-1]
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1ll11111l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11ll1111_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll11l11111_opy_: str):
        hook = PytestBDDFramework.bstack1ll11lll11l_opy_(instance, bstack1ll11l11111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1l111_opy_, []).clear()
    @staticmethod
    def __1ll111111ll_opy_(instance: bstack1lll1l1l1ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11ll1ll_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡧࡴࡸࡤࡴࠤው"), None)):
            return
        if os.getenv(bstack11ll1ll_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡑࡕࡇࡔࠤዎ"), bstack11ll1ll_opy_ (u"ࠨ࠱ࠣዏ")) != bstack11ll1ll_opy_ (u"ࠢ࠲ࠤዐ"):
            PytestBDDFramework.logger.warning(bstack11ll1ll_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡩ࡯ࡩࠣࡧࡦࡶ࡬ࡰࡩࠥዑ"))
            return
        bstack1ll111lll11_opy_ = {
            bstack11ll1ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣዒ"): (PytestBDDFramework.bstack1l1lllll11l_opy_, PytestBDDFramework.bstack1ll11l1111l_opy_),
            bstack11ll1ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧዓ"): (PytestBDDFramework.bstack1l1llllll11_opy_, PytestBDDFramework.bstack1ll111llll1_opy_),
        }
        for when in (bstack11ll1ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥዔ"), bstack11ll1ll_opy_ (u"ࠧࡩࡡ࡭࡮ࠥዕ"), bstack11ll1ll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣዖ")):
            bstack1l1lllll1ll_opy_ = args[1].get_records(when)
            if not bstack1l1lllll1ll_opy_:
                continue
            records = [
                bstack1l1llll111l_opy_(
                    kind=TestFramework.bstack1ll11111lll_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11ll1ll_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠥ዗")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11ll1ll_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࠤዘ")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1lllll1ll_opy_
                if isinstance(getattr(r, bstack11ll1ll_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥዙ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l1llll11ll_opy_, bstack1l1llll1l11_opy_ = bstack1ll111lll11_opy_.get(when, (None, None))
            bstack1ll11l11l11_opy_ = TestFramework.get_state(instance, bstack1l1llll11ll_opy_, None) if bstack1l1llll11ll_opy_ else None
            bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1l1llll1l11_opy_, None) if bstack1ll11l11l11_opy_ else None
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1ll11l11l11_opy_, [])) > 0:
                hook = bstack1ll11llllll_opy_[bstack1ll11l11l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1l111_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1l111_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll111l1111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1111ll1l_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1l1l11ll_opy_(request.node, scenario)
        bstack1ll111l11ll_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll111l11ll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll11llll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11llll_opy_: test_id,
            TestFramework.bstack1ll11ll11l1_opy_: test_name,
            TestFramework.bstack1ll111ll11l_opy_: test_id,
            TestFramework.bstack1ll1111l1l1_opy_: bstack1ll111l11ll_opy_,
            TestFramework.bstack1ll111l111l_opy_: PytestBDDFramework.__1ll1l1111ll_opy_(feature, scenario),
            TestFramework.bstack1l1llll1111_opy_: code,
            TestFramework.bstack1llll1111l1_opy_: TestFramework.bstack1l1lll1lll1_opy_,
            TestFramework.bstack1ll1lllll11_opy_: test_name
        }
    @staticmethod
    def __1ll1l1l11ll_opy_(node, scenario):
        if hasattr(node, bstack11ll1ll_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬዚ")):
            parts = node.nodeid.rsplit(bstack11ll1ll_opy_ (u"ࠦࡠࠨዛ"))
            params = parts[-1]
            return bstack11ll1ll_opy_ (u"ࠧࢁࡽࠡ࡝ࡾࢁࠧዜ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll1l1111ll_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11ll1ll_opy_ (u"࠭ࡴࡢࡩࡶࠫዝ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11ll1ll_opy_ (u"ࠧࡵࡣࡪࡷࠬዞ")) else [])
    @staticmethod
    def __1ll11ll111l_opy_(location):
        return bstack11ll1ll_opy_ (u"ࠣ࠼࠽ࠦዟ").join(filter(lambda x: isinstance(x, str), location))