# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llll1ll_opy_ import bstack1ll1l1lllll_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l1llllll_opy_ import bstack1ll111lllll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll111l_opy_,
    bstack1lll1l1ll1l_opy_,
    bstack1lll1ll1l1l_opy_,
    bstack1ll1l11ll1l_opy_,
    bstack1ll111lll1l_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l111l11_opy_
from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll1111l111_opy_ import bstack1ll11l111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l111l_opy_ import bstack1lll111llll_opy_
bstack1l1lllll1ll_opy_ = bstack1ll1l111l11_opy_()
bstack1ll11lll1l1_opy_ = bstack11111_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦሬ")
bstack1ll1111l1l1_opy_ = bstack11111_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣር")
bstack1ll111ll111_opy_ = bstack11111_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧሮ")
bstack1l1llllll11_opy_ = 1.0
_1l1llll1l1l_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1l1lll1lll1_opy_ = bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢሯ")
    bstack1ll1l1111ll_opy_ = bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨሰ")
    bstack1ll11l1l1ll_opy_ = bstack11111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣሱ")
    bstack1ll1l111lll_opy_ = bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧሲ")
    bstack1ll11ll1lll_opy_ = bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢሳ")
    bstack1l1lllll1l1_opy_: bool
    bstack1lll11l111l_opy_: bstack1lll111llll_opy_  = None
    bstack1ll1l1111l1_opy_ = [
        bstack1lll1ll111l_opy_.BEFORE_ALL,
        bstack1lll1ll111l_opy_.AFTER_ALL,
        bstack1lll1ll111l_opy_.BEFORE_EACH,
        bstack1lll1ll111l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll1l11l111_opy_: Dict[str, str],
        bstack1ll11llllll_opy_: List[str]=[bstack11111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤሴ")],
        bstack1lll11l111l_opy_: bstack1lll111llll_opy_ = None,
        bstack1llll1ll1ll_opy_=None
    ):
        super().__init__(bstack1ll11llllll_opy_, bstack1ll1l11l111_opy_, bstack1lll11l111l_opy_)
        self.bstack1l1lllll1l1_opy_ = any(bstack11111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥስ") in item.lower() for item in bstack1ll11llllll_opy_)
        self.bstack1llll1ll1ll_opy_ = bstack1llll1ll1ll_opy_
    def track_event(
        self,
        context: bstack1ll1l11ll1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1ll1l1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll111l_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1l1111l1_opy_:
            bstack1ll111lllll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll111l_opy_.NONE:
            self.logger.warning(bstack11111_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣሶ") + str(test_hook_state) + bstack11111_opy_ (u"ࠣࠤሷ"))
            return
        if not self.bstack1l1lllll1l1_opy_:
            self.logger.warning(bstack11111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥሸ") + str(str(self.bstack1ll11llllll_opy_)) + bstack11111_opy_ (u"ࠥࠦሹ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨሺ") + str(kwargs) + bstack11111_opy_ (u"ࠧࠨሻ"))
            return
        instance = self.__1l1llll1111_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧሼ") + str(args) + bstack11111_opy_ (u"ࠢࠣሽ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1111l1_opy_ and test_hook_state == bstack1lll1ll1l1l_opy_.PRE:
                bstack1ll11llll1l_opy_ = bstack1llll1ll1l1_opy_.bstack1ll1111lll1_opy_(EVENTS.bstack11111llll1_opy_.value)
                name = str(EVENTS.bstack11111llll1_opy_.name)+bstack11111_opy_ (u"ࠣ࠼ࠥሾ")+str(test_framework_state.name)
                TestFramework.bstack1ll1111ll11_opy_(instance, name, bstack1ll11llll1l_opy_)
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶࠥࡶࡲࡦ࠼ࠣࡿࢂࠨሿ").format(e))
        try:
            if test_framework_state == bstack1lll1ll111l_opy_.TEST:
                if not TestFramework.bstack1llllll1lll_opy_(instance, TestFramework.bstack1l1lll1l11l_opy_) and test_hook_state == bstack1lll1ll1l1l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11l11ll1_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11111_opy_ (u"ࠥࡰࡴࡧࡤࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥቀ") + str(test_hook_state) + bstack11111_opy_ (u"ࠦࠧቁ"))
                if test_hook_state == bstack1lll1ll1l1l_opy_.PRE and not TestFramework.bstack1llllll1lll_opy_(instance, TestFramework.bstack1l1lll1l1ll_opy_):
                    TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1l1lll1l1ll_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11ll11ll_opy_(instance, args)
                    self.logger.debug(bstack11111_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡴࡶࡤࡶࡹࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥቂ") + str(test_hook_state) + bstack11111_opy_ (u"ࠨࠢቃ"))
                elif test_hook_state == bstack1lll1ll1l1l_opy_.POST and not TestFramework.bstack1llllll1lll_opy_(instance, TestFramework.bstack1ll11l11l1l_opy_):
                    TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11l11l1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11111_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡨࡲࡩࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥቄ") + str(test_hook_state) + bstack11111_opy_ (u"ࠣࠤቅ"))
            elif test_framework_state == bstack1lll1ll111l_opy_.STEP:
                if test_hook_state == bstack1lll1ll1l1l_opy_.PRE:
                    PytestBDDFramework.__1ll111l1111_opy_(instance, args)
                elif test_hook_state == bstack1lll1ll1l1l_opy_.POST:
                    PytestBDDFramework.__1l1lll1ll1l_opy_(instance, args)
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG and test_hook_state == bstack1lll1ll1l1l_opy_.POST:
                PytestBDDFramework.__1ll1111111l_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG_REPORT and test_hook_state == bstack1lll1ll1l1l_opy_.POST:
                self.__1ll1111l11l_opy_(instance, *args)
                self.__1ll11l1111l_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1l1111l1_opy_:
                self.__1ll11111111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥቆ") + str(instance.ref()) + bstack11111_opy_ (u"ࠥࠦቇ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11lllll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1111l1_opy_ and test_hook_state == bstack1lll1ll1l1l_opy_.POST:
                name = str(EVENTS.bstack11111llll1_opy_.name)+bstack11111_opy_ (u"ࠦ࠿ࠨቈ")+str(test_framework_state.name)
                bstack1ll11llll1l_opy_ = TestFramework.bstack1ll11111lll_opy_(instance, name)
                bstack1llll1ll1l1_opy_.end(EVENTS.bstack11111llll1_opy_.value, bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ቉"), bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦቊ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢቋ").format(e))
    def bstack1ll11l11l11_opy_(self):
        return self.bstack1l1lllll1l1_opy_
    def __1ll111l1lll_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11111_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧቌ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1lllll11l_opy_(rep, [bstack11111_opy_ (u"ࠤࡺ࡬ࡪࡴࠢቍ"), bstack11111_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦ቎"), bstack11111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ቏"), bstack11111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧቐ"), bstack11111_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢቑ"), bstack11111_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨቒ")])
        return None
    def __1ll1111l11l_opy_(self, instance: bstack1lll1l1ll1l_opy_, *args):
        result = self.__1ll111l1lll_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111111ll_opy_ = None
        if result.get(bstack11111_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤቓ"), None) == bstack11111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤቔ") and len(args) > 1 and getattr(args[1], bstack11111_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦቕ"), None) is not None:
            failure = [{bstack11111_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧቖ"): [args[1].excinfo.exconly(), result.get(bstack11111_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦ቗"), None)]}]
            bstack11111111ll_opy_ = bstack11111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢቘ") if bstack11111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ቙") in getattr(args[1].excinfo, bstack11111_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥቚ"), bstack11111_opy_ (u"ࠤࠥቛ")) else bstack11111_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦቜ")
        bstack1ll11ll1111_opy_ = result.get(bstack11111_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧቝ"), TestFramework.bstack1ll11l1l11l_opy_)
        if bstack1ll11ll1111_opy_ != TestFramework.bstack1ll11l1l11l_opy_:
            TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll111l11ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11l1ll1l_opy_(instance, {
            TestFramework.bstack1lll1l11lll_opy_: failure,
            TestFramework.bstack1ll1111llll_opy_: bstack11111111ll_opy_,
            TestFramework.bstack1lll11llll1_opy_: bstack1ll11ll1111_opy_,
        })
    def __1l1llll1111_opy_(
        self,
        context: bstack1ll1l11ll1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1ll1l1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll111l_opy_.SETUP_FIXTURE:
            instance = self.__1l1lll1l111_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11lll1ll_opy_ bstack1ll11l1ll11_opy_ this to be bstack11111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ቞")
            if test_framework_state == bstack1lll1ll111l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11111l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11111_opy_ (u"ࠨ࡮ࡰࡦࡨࠦ቟"), None), bstack11111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢበ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11111_opy_ (u"ࠣࡰࡲࡨࡪࠨቡ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤቢ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111llll1_opy_(target) if target else None
        return instance
    def __1ll11111111_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1ll1l1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l11lll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l1111ll_opy_, {})
        if not key in bstack1ll1l11lll1_opy_:
            bstack1ll1l11lll1_opy_[key] = []
        bstack1ll11ll1l1l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l1l1ll_opy_, {})
        if not key in bstack1ll11ll1l1l_opy_:
            bstack1ll11ll1l1l_opy_[key] = []
        bstack1ll1l1l111l_opy_ = {
            PytestBDDFramework.bstack1ll1l1111ll_opy_: bstack1ll1l11lll1_opy_,
            PytestBDDFramework.bstack1ll11l1l1ll_opy_: bstack1ll11ll1l1l_opy_,
        }
        if test_hook_state == bstack1lll1ll1l1l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11111_opy_ (u"ࠥ࡯ࡪࡿࠢባ"): key,
                TestFramework.bstack1ll1l1l1l1l_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l11111_opy_: TestFramework.bstack1ll11ll1l11_opy_,
                TestFramework.bstack1l1llllll1l_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1l11llll_opy_: [],
                TestFramework.bstack1l1llll11ll_opy_: hook_name,
                TestFramework.bstack1ll111l1l11_opy_: bstack1ll11l111ll_opy_.bstack1ll11lll111_opy_()
            }
            bstack1ll1l11lll1_opy_[key].append(hook)
            bstack1ll1l1l111l_opy_[PytestBDDFramework.bstack1ll1l111lll_opy_] = key
        elif test_hook_state == bstack1lll1ll1l1l_opy_.POST:
            bstack1ll11ll11l1_opy_ = bstack1ll1l11lll1_opy_.get(key, [])
            hook = bstack1ll11ll11l1_opy_.pop() if bstack1ll11ll11l1_opy_ else None
            if hook:
                result = self.__1ll111l1lll_opy_(*args)
                if result:
                    bstack1ll1l1l1111_opy_ = result.get(bstack11111_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧቤ"), TestFramework.bstack1ll11ll1l11_opy_)
                    if bstack1ll1l1l1111_opy_ != TestFramework.bstack1ll11ll1l11_opy_:
                        hook[TestFramework.bstack1ll11l11111_opy_] = bstack1ll1l1l1111_opy_
                hook[TestFramework.bstack1ll111ll1ll_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll111l1l11_opy_] = bstack1ll11l111ll_opy_.bstack1ll11lll111_opy_()
                self.bstack1ll111l111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l111111_opy_, [])
                self.bstack1ll1l111l1l_opy_(instance, logs)
                bstack1ll11ll1l1l_opy_[key].append(hook)
                bstack1ll1l1l111l_opy_[PytestBDDFramework.bstack1ll11ll1lll_opy_] = key
        TestFramework.bstack1ll11l1ll1l_opy_(instance, bstack1ll1l1l111l_opy_)
        self.logger.debug(bstack11111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦብ") + str(bstack1ll11ll1l1l_opy_) + bstack11111_opy_ (u"ࠨࠢቦ"))
    def __1l1lll1l111_opy_(
        self,
        context: bstack1ll1l11ll1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1ll1l1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1lllll11l_opy_(args[0], [bstack11111_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨቧ"), bstack11111_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤቨ"), bstack11111_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤቩ"), bstack11111_opy_ (u"ࠥ࡭ࡩࡹࠢቪ"), bstack11111_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨቫ"), bstack11111_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧቬ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11111_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቭ")) else fixturedef.get(bstack11111_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨቮ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11111_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨቯ")) else None
        node = request.node if hasattr(request, bstack11111_opy_ (u"ࠤࡱࡳࡩ࡫ࠢተ")) else None
        target = request.node.nodeid if hasattr(node, bstack11111_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥቱ")) else None
        baseid = fixturedef.get(bstack11111_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦቲ"), None) or bstack11111_opy_ (u"ࠧࠨታ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11111_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦቴ")):
            target = PytestBDDFramework.__1ll1l1l1l11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11111_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤት")) else None
            if target and not TestFramework.bstack1ll111llll1_opy_(target):
                self.__1ll1l11111l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥቶ") + str(test_hook_state) + bstack11111_opy_ (u"ࠤࠥቷ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣቸ") + str(target) + bstack11111_opy_ (u"ࠦࠧቹ"))
            return None
        instance = TestFramework.bstack1ll111llll1_opy_(target)
        if not instance:
            self.logger.warning(bstack11111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢቺ") + str(target) + bstack11111_opy_ (u"ࠨࠢቻ"))
            return None
        bstack1ll11l1llll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1lll1lll1_opy_, {})
        if os.getenv(bstack11111_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣቼ"), bstack11111_opy_ (u"ࠣ࠳ࠥች")) == bstack11111_opy_ (u"ࠤ࠴ࠦቾ"):
            bstack1ll1l1l11l1_opy_ = bstack11111_opy_ (u"ࠥ࠾ࠧቿ").join((scope, fixturename))
            bstack1ll1l11l1ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11llll11_opy_ = {
                bstack11111_opy_ (u"ࠦࡰ࡫ࡹࠣኀ"): bstack1ll1l1l11l1_opy_,
                bstack11111_opy_ (u"ࠧࡺࡡࡨࡵࠥኁ"): PytestBDDFramework.__1ll111111l1_opy_(request.node, scenario),
                bstack11111_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢኂ"): fixturedef,
                bstack11111_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨኃ"): scope,
                bstack11111_opy_ (u"ࠣࡶࡼࡴࡪࠨኄ"): None,
            }
            try:
                if test_hook_state == bstack1lll1ll1l1l_opy_.POST and callable(getattr(args[-1], bstack11111_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨኅ"), None)):
                    bstack1ll11llll11_opy_[bstack11111_opy_ (u"ࠥࡸࡾࡶࡥࠣኆ")] = TestFramework.bstack1ll1l11ll11_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1ll1l1l_opy_.PRE:
                bstack1ll11llll11_opy_[bstack11111_opy_ (u"ࠦࡺࡻࡩࡥࠤኇ")] = uuid4().__str__()
                bstack1ll11llll11_opy_[PytestBDDFramework.bstack1l1llllll1l_opy_] = bstack1ll1l11l1ll_opy_
            elif test_hook_state == bstack1lll1ll1l1l_opy_.POST:
                bstack1ll11llll11_opy_[PytestBDDFramework.bstack1ll111ll1ll_opy_] = bstack1ll1l11l1ll_opy_
            if bstack1ll1l1l11l1_opy_ in bstack1ll11l1llll_opy_:
                bstack1ll11l1llll_opy_[bstack1ll1l1l11l1_opy_].update(bstack1ll11llll11_opy_)
                self.logger.debug(bstack11111_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨኈ") + str(bstack1ll11l1llll_opy_[bstack1ll1l1l11l1_opy_]) + bstack11111_opy_ (u"ࠨࠢ኉"))
            else:
                bstack1ll11l1llll_opy_[bstack1ll1l1l11l1_opy_] = bstack1ll11llll11_opy_
                self.logger.debug(bstack11111_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥኊ") + str(len(bstack1ll11l1llll_opy_)) + bstack11111_opy_ (u"ࠣࠤኋ"))
        TestFramework.bstack1lllllll11l_opy_(instance, PytestBDDFramework.bstack1l1lll1lll1_opy_, bstack1ll11l1llll_opy_)
        self.logger.debug(bstack11111_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤኌ") + str(instance.ref()) + bstack11111_opy_ (u"ࠥࠦኍ"))
        return instance
    def __1ll1l11111l_opy_(
        self,
        context: bstack1ll1l11ll1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1l1lllll_opy_.create_context(target)
        ob = bstack1lll1l1ll1l_opy_(ctx, self.bstack1ll11llllll_opy_, self.bstack1ll1l11l111_opy_, test_framework_state)
        TestFramework.bstack1ll11l1ll1l_opy_(ob, {
            TestFramework.bstack1lll11l11l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll11lll1l_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1l111_opy_: [],
            PytestBDDFramework.bstack1l1lll1lll1_opy_: {},
            PytestBDDFramework.bstack1ll11l1l1ll_opy_: {},
            PytestBDDFramework.bstack1ll1l1111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllllll11l_opy_(ob, TestFramework.bstack1ll111l1l1l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllllll11l_opy_(ob, TestFramework.bstack1lllll1ll11_opy_, context.platform_index)
        TestFramework.bstack1lll1l1l1l1_opy_[ctx.id] = ob
        self.logger.debug(bstack11111_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦ኎") + str(TestFramework.bstack1lll1l1l1l1_opy_.keys()) + bstack11111_opy_ (u"ࠧࠨ኏"))
        return ob
    @staticmethod
    def __1ll11ll11ll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11111_opy_ (u"࠭ࡩࡥࠩነ"): id(step),
                bstack11111_opy_ (u"ࠧࡵࡧࡻࡸࠬኑ"): step.name,
                bstack11111_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩኒ"): step.keyword,
            })
        meta = {
            bstack11111_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪና"): {
                bstack11111_opy_ (u"ࠪࡲࡦࡳࡥࠨኔ"): feature.name,
                bstack11111_opy_ (u"ࠫࡵࡧࡴࡩࠩን"): feature.filename,
                bstack11111_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪኖ"): feature.description
            },
            bstack11111_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨኗ"): {
                bstack11111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬኘ"): scenario.name
            },
            bstack11111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኙ"): steps,
            bstack11111_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫኚ"): PytestBDDFramework.__1ll11l1lll1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l1llll11l1_opy_: meta
            }
        )
    def bstack1ll111l111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡵ࡬ࡱ࡮ࡲࡡࡳࠢࡷࡳࠥࡺࡨࡦࠢࡍࡥࡻࡧࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡯ࡳࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡄࡪࡨࡧࡰࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࡭ࡳࡹࡩࡥࡧࠣࢂ࠴࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠴࡛ࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡊࡴࡸࠠࡦࡣࡦ࡬ࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠮ࠣࡶࡪࡶ࡬ࡢࡥࡨࡷࠥࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧࠦࡩ࡯ࠢ࡬ࡸࡸࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡍ࡫ࠦࡡࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡰࡥࡹࡩࡨࡦࡵࠣࡥࠥࡳ࡯ࡥ࡫ࡩ࡭ࡪࡪࠠࡩࡱࡲ࡯࠲ࡲࡥࡷࡧ࡯ࠤ࡫࡯࡬ࡦ࠮ࠣ࡭ࡹࠦࡣࡳࡧࡤࡸࡪࡹࠠࡢࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࠤࡼ࡯ࡴࡩࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡓࡪ࡯࡬ࡰࡦࡸ࡬ࡺ࠮ࠣ࡭ࡹࠦࡰࡳࡱࡦࡩࡸࡹࡥࡴࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡱࡵࡣࡢࡶࡨࡨࠥ࡯࡮ࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡦࡾࠦࡲࡦࡲ࡯ࡥࡨ࡯࡮ࡨࠢࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡗ࡬ࡪࠦࡣࡳࡧࡤࡸࡪࡪࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡥࡷ࡫ࠠࡢࡦࡧࡩࡩࠦࡴࡰࠢࡷ࡬ࡪࠦࡨࡰࡱ࡮ࠫࡸࠦࠢ࡭ࡱࡪࡷࠧࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫࠻ࠢࡗ࡬ࡪࠦࡥࡷࡧࡱࡸࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࠦࡡ࡯ࡦࠣ࡬ࡴࡵ࡫ࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤ࡙࡫ࡳࡵࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤኛ")
        global _1l1llll1l1l_opy_
        platform_index = os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫኜ")]
        bstack1ll111ll11l_opy_ = os.path.join(bstack1l1lllll1ll_opy_, (bstack1ll11lll1l1_opy_ + str(platform_index)), bstack1ll1111l1l1_opy_)
        if not os.path.exists(bstack1ll111ll11l_opy_) or not os.path.isdir(bstack1ll111ll11l_opy_):
            return
        logs = hook.get(bstack11111_opy_ (u"ࠧࡲ࡯ࡨࡵࠥኝ"), [])
        with os.scandir(bstack1ll111ll11l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1l1llll1l1l_opy_:
                    self.logger.info(bstack11111_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦኞ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11111_opy_ (u"ࠢࠣኟ")
                    log_entry = bstack1ll111lll1l_opy_(
                        kind=bstack11111_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥአ"),
                        message=bstack11111_opy_ (u"ࠤࠥኡ"),
                        level=bstack11111_opy_ (u"ࠥࠦኢ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1lllllll1_opy_=entry.stat().st_size,
                        bstack1l1llll111l_opy_=bstack11111_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦኣ"),
                        bstack11ll111_opy_=os.path.abspath(entry.path),
                        bstack1l1llll1l11_opy_=hook.get(TestFramework.bstack1ll1l1l1l1l_opy_)
                    )
                    logs.append(log_entry)
                    _1l1llll1l1l_opy_.add(abs_path)
        platform_index = os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬኤ")]
        bstack1ll111l1ll1_opy_ = os.path.join(bstack1l1lllll1ll_opy_, (bstack1ll11lll1l1_opy_ + str(platform_index)), bstack1ll1111l1l1_opy_, bstack1ll111ll111_opy_)
        if not os.path.exists(bstack1ll111l1ll1_opy_) or not os.path.isdir(bstack1ll111l1ll1_opy_):
            self.logger.info(bstack11111_opy_ (u"ࠨࡎࡰࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡩࡳࡺࡴࡤࠡࡣࡷ࠾ࠥࢁࡽࠣእ").format(bstack1ll111l1ll1_opy_))
        else:
            self.logger.info(bstack11111_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡨࡵࡳࡲࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠼ࠣࡿࢂࠨኦ").format(bstack1ll111l1ll1_opy_))
            with os.scandir(bstack1ll111l1ll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1l1llll1l1l_opy_:
                        self.logger.info(bstack11111_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨኧ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11111_opy_ (u"ࠤࠥከ")
                        log_entry = bstack1ll111lll1l_opy_(
                            kind=bstack11111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧኩ"),
                            message=bstack11111_opy_ (u"ࠦࠧኪ"),
                            level=bstack11111_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤካ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1lllllll1_opy_=entry.stat().st_size,
                            bstack1l1llll111l_opy_=bstack11111_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨኬ"),
                            bstack11ll111_opy_=os.path.abspath(entry.path),
                            bstack1ll11l111l1_opy_=hook.get(TestFramework.bstack1ll1l1l1l1l_opy_)
                        )
                        logs.append(log_entry)
                        _1l1llll1l1l_opy_.add(abs_path)
        hook[bstack11111_opy_ (u"ࠢ࡭ࡱࡪࡷࠧክ")] = logs
    def bstack1ll1l111l1l_opy_(
        self,
        bstack1l1llll1ll1_opy_: bstack1lll1l1ll1l_opy_,
        entries: List[bstack1ll111lll1l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧኮ"))
        req.platform_index = TestFramework.get_state(bstack1l1llll1ll1_opy_, TestFramework.bstack1lllll1ll11_opy_)
        req.execution_context.hash = str(bstack1l1llll1ll1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1llll1ll1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1llll1ll1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1llll1ll1_opy_, TestFramework.bstack1lll11l11l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1llll1ll1_opy_, TestFramework.bstack1lll11lll1l_opy_)
            log_entry.uuid = entry.bstack1l1llll1l11_opy_ if entry.bstack1l1llll1l11_opy_ else TestFramework.get_state(bstack1l1llll1ll1_opy_, TestFramework.bstack1lll1lll1ll_opy_)
            log_entry.test_framework_state = bstack1l1llll1ll1_opy_.state.name
            log_entry.message = entry.message.encode(bstack11111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣኯ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧኰ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1lllllll1_opy_
                log_entry.file_path = entry.bstack11ll111_opy_
        def bstack1l1lll11lll_opy_():
            bstack11lll11111_opy_ = datetime.now()
            try:
                self.bstack1llll1ll1ll_opy_.LogCreatedEvent(req)
                bstack1l1llll1ll1_opy_.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠣ኱"), datetime.now() - bstack11lll11111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡽࢀࠦኲ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l111l_opy_.enqueue(bstack1l1lll11lll_opy_)
    def __1ll11l1111l_opy_(self, instance) -> None:
        bstack11111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡐࡴࡧࡤࡴࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࡹࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡲࡦࡣࡷࡩࡸࠦࡡࠡࡦ࡬ࡧࡹࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡸࡪࡹࡴࠡ࡮ࡨࡺࡪࡲࠠࡤࡷࡶࡸࡴࡳࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡻࡳࡵࡱࡰࡘࡦ࡭ࡍࡢࡰࡤ࡫ࡪࡸࠠࡢࡰࡧࠤࡺࡶࡤࡢࡶࡨࡷࠥࡺࡨࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡸࡺࡡࡵࡧࠣࡹࡸ࡯࡮ࡨࠢࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኳ")
        bstack1ll1l1l111l_opy_ = {bstack11111_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠤኴ"): bstack1ll11l111ll_opy_.bstack1ll11lll111_opy_()}
        TestFramework.bstack1ll11l1ll1l_opy_(instance, bstack1ll1l1l111l_opy_)
    @staticmethod
    def __1ll111l1111_opy_(instance, args):
        request, bstack1ll111111ll_opy_ = args
        bstack1ll11l11lll_opy_ = id(bstack1ll111111ll_opy_)
        bstack1ll11111l1l_opy_ = instance.data[TestFramework.bstack1l1llll11l1_opy_]
        step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠨ࡫ࡧࠫኵ")] == bstack1ll11l11lll_opy_, bstack1ll11111l1l_opy_[bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ኶")]), None)
        step.update({
            bstack11111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ኷"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11111l1l_opy_[bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኸ")]) if st[bstack11111_opy_ (u"ࠬ࡯ࡤࠨኹ")] == step[bstack11111_opy_ (u"࠭ࡩࡥࠩኺ")]), None)
        if index is not None:
            bstack1ll11111l1l_opy_[bstack11111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኻ")][index] = step
        instance.data[TestFramework.bstack1l1llll11l1_opy_] = bstack1ll11111l1l_opy_
    @staticmethod
    def __1l1lll1ll1l_opy_(instance, args):
        bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡽࡨࡦࡰࠣࡰࡪࡴࠠࡢࡴࡪࡷࠥ࡯ࡳࠡ࠴࠯ࠤ࡮ࡺࠠࡴ࡫ࡪࡲ࡮࡬ࡩࡦࡵࠣࡸ࡭࡫ࡲࡦࠢ࡬ࡷࠥࡴ࡯ࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࡹࠠࡢࡴࡨࠤ࠲࡛ࠦࡳࡧࡴࡹࡪࡹࡴ࠭ࠢࡶࡸࡪࡶ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡧࡲࡨࡵࠣࡥࡷ࡫ࠠ࠴ࠢࡷ࡬ࡪࡴࠠࡵࡪࡨࠤࡱࡧࡳࡵࠢࡹࡥࡱࡻࡥࠡ࡫ࡶࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኼ")
        bstack1ll1111l1ll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll111111ll_opy_ = args[1]
        bstack1ll11l11lll_opy_ = id(bstack1ll111111ll_opy_)
        bstack1ll11111l1l_opy_ = instance.data[TestFramework.bstack1l1llll11l1_opy_]
        step = None
        if bstack1ll11l11lll_opy_ is not None and bstack1ll11111l1l_opy_.get(bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኽ")):
            step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠪ࡭ࡩ࠭ኾ")] == bstack1ll11l11lll_opy_, bstack1ll11111l1l_opy_[bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ኿")]), None)
            step.update({
                bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪዀ"): bstack1ll1111l1ll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭዁"): bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧዂ"),
                bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩዃ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩዄ"): bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪዅ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11111l1l_opy_[bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ዆")]) if st[bstack11111_opy_ (u"ࠬ࡯ࡤࠨ዇")] == step[bstack11111_opy_ (u"࠭ࡩࡥࠩወ")]), None)
        if index is not None:
            bstack1ll11111l1l_opy_[bstack11111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ዉ")][index] = step
        instance.data[TestFramework.bstack1l1llll11l1_opy_] = bstack1ll11111l1l_opy_
    @staticmethod
    def __1ll11l1lll1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11111_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪዊ")):
                examples = list(node.callspec.params[bstack11111_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨዋ")].values())
            return examples
        except:
            return []
    def bstack1ll111lll11_opy_(self, instance: bstack1lll1l1ll1l_opy_, bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_]):
        bstack1ll1l1l11ll_opy_ = (
            PytestBDDFramework.bstack1ll1l111lll_opy_
            if bstack1llll11ll1l_opy_[1] == bstack1lll1ll1l1l_opy_.PRE
            else PytestBDDFramework.bstack1ll11ll1lll_opy_
        )
        hook = PytestBDDFramework.bstack1ll11ll111l_opy_(instance, bstack1ll1l1l11ll_opy_)
        entries = hook.get(TestFramework.bstack1ll1l11llll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1l111_opy_, []))
        return entries
    def bstack1ll11111l11_opy_(self, instance: bstack1lll1l1ll1l_opy_, bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_]):
        bstack1ll1l1l11ll_opy_ = (
            PytestBDDFramework.bstack1ll1l111lll_opy_
            if bstack1llll11ll1l_opy_[1] == bstack1lll1ll1l1l_opy_.PRE
            else PytestBDDFramework.bstack1ll11ll1lll_opy_
        )
        PytestBDDFramework.bstack1l1lll1llll_opy_(instance, bstack1ll1l1l11ll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1l111_opy_, []).clear()
    @staticmethod
    def bstack1ll11ll111l_opy_(instance: bstack1lll1l1ll1l_opy_, bstack1ll1l1l11ll_opy_: str):
        bstack1l1lll1l1l1_opy_ = (
            PytestBDDFramework.bstack1ll11l1l1ll_opy_
            if bstack1ll1l1l11ll_opy_ == PytestBDDFramework.bstack1ll11ll1lll_opy_
            else PytestBDDFramework.bstack1ll1l1111ll_opy_
        )
        bstack1ll11ll1ll1_opy_ = TestFramework.get_state(instance, bstack1ll1l1l11ll_opy_, None)
        bstack1ll1l111ll1_opy_ = TestFramework.get_state(instance, bstack1l1lll1l1l1_opy_, None) if bstack1ll11ll1ll1_opy_ else None
        return (
            bstack1ll1l111ll1_opy_[bstack1ll11ll1ll1_opy_][-1]
            if isinstance(bstack1ll1l111ll1_opy_, dict) and len(bstack1ll1l111ll1_opy_.get(bstack1ll11ll1ll1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l1lll1llll_opy_(instance: bstack1lll1l1ll1l_opy_, bstack1ll1l1l11ll_opy_: str):
        hook = PytestBDDFramework.bstack1ll11ll111l_opy_(instance, bstack1ll1l1l11ll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1l11llll_opy_, []).clear()
    @staticmethod
    def __1ll1111111l_opy_(instance: bstack1lll1l1ll1l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡦࡳࡷࡪࡳࠣዌ"), None)):
            return
        if os.getenv(bstack11111_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡐࡔࡍࡓࠣው"), bstack11111_opy_ (u"ࠧ࠷ࠢዎ")) != bstack11111_opy_ (u"ࠨ࠱ࠣዏ"):
            PytestBDDFramework.logger.warning(bstack11111_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡯࡮ࡨࠢࡦࡥࡵࡲ࡯ࡨࠤዐ"))
            return
        bstack1ll1111ll1l_opy_ = {
            bstack11111_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢዑ"): (PytestBDDFramework.bstack1ll1l111lll_opy_, PytestBDDFramework.bstack1ll1l1111ll_opy_),
            bstack11111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦዒ"): (PytestBDDFramework.bstack1ll11ll1lll_opy_, PytestBDDFramework.bstack1ll11l1l1ll_opy_),
        }
        for when in (bstack11111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤዓ"), bstack11111_opy_ (u"ࠦࡨࡧ࡬࡭ࠤዔ"), bstack11111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢዕ")):
            bstack1l1llll1lll_opy_ = args[1].get_records(when)
            if not bstack1l1llll1lll_opy_:
                continue
            records = [
                bstack1ll111lll1l_opy_(
                    kind=TestFramework.bstack1ll11lll11l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11111_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠤዖ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11111_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࠣ዗")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1llll1lll_opy_
                if isinstance(getattr(r, bstack11111_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤዘ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l1l1l1_opy_, bstack1l1lll1l1l1_opy_ = bstack1ll1111ll1l_opy_.get(when, (None, None))
            bstack1l1llllllll_opy_ = TestFramework.get_state(instance, bstack1ll11l1l1l1_opy_, None) if bstack1ll11l1l1l1_opy_ else None
            bstack1ll1l111ll1_opy_ = TestFramework.get_state(instance, bstack1l1lll1l1l1_opy_, None) if bstack1l1llllllll_opy_ else None
            if isinstance(bstack1ll1l111ll1_opy_, dict) and len(bstack1ll1l111ll1_opy_.get(bstack1l1llllllll_opy_, [])) > 0:
                hook = bstack1ll1l111ll1_opy_[bstack1l1llllllll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1l11llll_opy_ in hook:
                    hook[TestFramework.bstack1ll1l11llll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1l111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11l11ll1_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1l11l1l1_opy_(request.node, scenario)
        bstack1ll11111ll1_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll11111ll1_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1lll1ll_opy_: uuid4().__str__(),
            TestFramework.bstack1l1lll1l11l_opy_: test_id,
            TestFramework.bstack1ll1l11l11l_opy_: test_name,
            TestFramework.bstack1ll111ll1l1_opy_: test_id,
            TestFramework.bstack1l1lll1ll11_opy_: bstack1ll11111ll1_opy_,
            TestFramework.bstack1l1lllll111_opy_: PytestBDDFramework.__1ll111111l1_opy_(feature, scenario),
            TestFramework.bstack1ll111l11l1_opy_: code,
            TestFramework.bstack1lll11llll1_opy_: TestFramework.bstack1ll11l1l11l_opy_,
            TestFramework.bstack1ll1lllll11_opy_: test_name
        }
    @staticmethod
    def __1ll1l11l1l1_opy_(node, scenario):
        if hasattr(node, bstack11111_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫዙ")):
            parts = node.nodeid.rsplit(bstack11111_opy_ (u"ࠥ࡟ࠧዚ"))
            params = parts[-1]
            return bstack11111_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦዛ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll111111l1_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11111_opy_ (u"ࠬࡺࡡࡨࡵࠪዜ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11111_opy_ (u"࠭ࡴࡢࡩࡶࠫዝ")) else [])
    @staticmethod
    def __1ll1l1l1l11_opy_(location):
        return bstack11111_opy_ (u"ࠢ࠻࠼ࠥዞ").join(filter(lambda x: isinstance(x, str), location))