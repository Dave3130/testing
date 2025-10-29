# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1ll11111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1lllll1111_opy_ import bstack1l1lll1ll1l_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1l11l_opy_,
    bstack1lll1l11lll_opy_,
    bstack1lll11lll1l_opy_,
    bstack1ll1l1l11l1_opy_,
    bstack1ll11lll11l_opy_,
)
import traceback
from bstack_utils.helper import bstack1l1lll1l111_opy_
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll111ll11l_opy_ import bstack1ll1l1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
bstack1ll1111l111_opy_ = bstack1l1lll1l111_opy_()
bstack1l1llll1lll_opy_ = bstack11ll1l_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢረ")
bstack1ll11l11l11_opy_ = bstack11ll1l_opy_ (u"ࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦሩ")
bstack1ll1l1111ll_opy_ = bstack11ll1l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣሪ")
bstack1l1lllll1ll_opy_ = 1.0
_1l1llllllll_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l11111l_opy_ = bstack11ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥራ")
    bstack1ll1111l11l_opy_ = bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࠤሬ")
    bstack1l1llll1ll1_opy_ = bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦር")
    bstack1ll1l11lll1_opy_ = bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣሮ")
    bstack1ll1l11ll11_opy_ = bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥሯ")
    bstack1ll111ll111_opy_: bool
    bstack1lll11l11l1_opy_: bstack1lll11l111l_opy_  = None
    bstack1ll1l111111_opy_ = [
        bstack1lll1l1l11l_opy_.BEFORE_ALL,
        bstack1lll1l1l11l_opy_.AFTER_ALL,
        bstack1lll1l1l11l_opy_.BEFORE_EACH,
        bstack1lll1l1l11l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11ll1111_opy_: Dict[str, str],
        bstack1ll111l11l1_opy_: List[str]=[bstack11ll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧሰ")],
        bstack1lll11l11l1_opy_: bstack1lll11l111l_opy_ = None,
        bstack1lllll111l1_opy_=None
    ):
        super().__init__(bstack1ll111l11l1_opy_, bstack1ll11ll1111_opy_, bstack1lll11l11l1_opy_)
        self.bstack1ll111ll111_opy_ = any(bstack11ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨሱ") in item.lower() for item in bstack1ll111l11l1_opy_)
        self.bstack1lllll111l1_opy_ = bstack1lllll111l1_opy_
    def track_event(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1lll1l1l11l_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1l11l_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1l111111_opy_:
            bstack1l1lll1ll1l_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1l11l_opy_.NONE:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧࡧࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࠦሲ") + str(test_hook_state) + bstack11ll1l_opy_ (u"ࠦࠧሳ"))
            return
        if not self.bstack1ll111ll111_opy_:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡂࠨሴ") + str(str(self.bstack1ll111l11l1_opy_)) + bstack11ll1l_opy_ (u"ࠨࠢስ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤሶ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠣࠤሷ"))
            return
        instance = self.__1ll1l1l111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡤࡶ࡬ࡹ࠽ࠣሸ") + str(args) + bstack11ll1l_opy_ (u"ࠥࠦሹ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l111111_opy_ and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll111l1l1l_opy_ = bstack1llll111ll1_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack1l111lll1_opy_.value)
                name = str(EVENTS.bstack1l111lll1_opy_.name)+bstack11ll1l_opy_ (u"ࠦ࠿ࠨሺ")+str(test_framework_state.name)
                TestFramework.bstack1ll111l111l_opy_(instance, name, bstack1ll111l1l1l_opy_)
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲࠡࡲࡵࡩ࠿ࠦࡻࡾࠤሻ").format(e))
        try:
            if test_framework_state == bstack1lll1l1l11l_opy_.TEST:
                if not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11l1111l_opy_) and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11111lll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡬ࡰࡣࡧࡩࡩࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨሼ") + str(test_hook_state) + bstack11ll1l_opy_ (u"ࠢࠣሽ"))
                if test_hook_state == bstack1lll11lll1l_opy_.PRE and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_):
                    TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11lll1ll_opy_(instance, args)
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡷࡹࡧࡲࡵࠢࡩࡳࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨሾ") + str(test_hook_state) + bstack11ll1l_opy_ (u"ࠤࠥሿ"))
                elif test_hook_state == bstack1lll11lll1l_opy_.POST and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll111ll1l1_opy_):
                    TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1ll111ll1l1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲࡫࡮ࡥࠢࡩࡳࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨቀ") + str(test_hook_state) + bstack11ll1l_opy_ (u"ࠦࠧቁ"))
            elif test_framework_state == bstack1lll1l1l11l_opy_.STEP:
                if test_hook_state == bstack1lll11lll1l_opy_.PRE:
                    PytestBDDFramework.__1l1lllll11l_opy_(instance, args)
                elif test_hook_state == bstack1lll11lll1l_opy_.POST:
                    PytestBDDFramework.__1ll111111l1_opy_(instance, args)
            elif test_framework_state == bstack1lll1l1l11l_opy_.LOG and test_hook_state == bstack1lll11lll1l_opy_.POST:
                PytestBDDFramework.__1ll1l1l1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1l11l_opy_.LOG_REPORT and test_hook_state == bstack1lll11lll1l_opy_.POST:
                self.__1ll11l111ll_opy_(instance, *args)
                self.__1ll1111ll11_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1l111111_opy_:
                self.__1l1lllllll1_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨቂ") + str(instance.ref()) + bstack11ll1l_opy_ (u"ࠨࠢቃ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11ll1l1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l111111_opy_ and test_hook_state == bstack1lll11lll1l_opy_.POST:
                name = str(EVENTS.bstack1l111lll1_opy_.name)+bstack11ll1l_opy_ (u"ࠢ࠻ࠤቄ")+str(test_framework_state.name)
                bstack1ll111l1l1l_opy_ = TestFramework.bstack1l1lll1l1ll_opy_(instance, name)
                bstack1llll111ll1_opy_.end(EVENTS.bstack1l111lll1_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣቅ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢቆ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥቇ").format(e))
    def bstack1ll1l1l11ll_opy_(self):
        return self.bstack1ll111ll111_opy_
    def __1ll1111111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11ll1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣቈ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111llll1_opy_(rep, [bstack11ll1l_opy_ (u"ࠧࡽࡨࡦࡰࠥ቉"), bstack11ll1l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢቊ"), bstack11ll1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢቋ"), bstack11ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣቌ"), bstack11ll1l_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠥቍ"), bstack11ll1l_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤ቎")])
        return None
    def __1ll11l111ll_opy_(self, instance: bstack1lll1l11lll_opy_, *args):
        result = self.__1ll1111111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111111ll_opy_ = None
        if result.get(bstack11ll1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧ቏"), None) == bstack11ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧቐ") and len(args) > 1 and getattr(args[1], bstack11ll1l_opy_ (u"ࠨࡥࡹࡥ࡬ࡲ࡫ࡵࠢቑ"), None) is not None:
            failure = [{bstack11ll1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪቒ"): [args[1].excinfo.exconly(), result.get(bstack11ll1l_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢቓ"), None)]}]
            bstack11111111ll_opy_ = bstack11ll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥቔ") if bstack11ll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨቕ") in getattr(args[1].excinfo, bstack11ll1l_opy_ (u"ࠦࡹࡿࡰࡦࡰࡤࡱࡪࠨቖ"), bstack11ll1l_opy_ (u"ࠧࠨ቗")) else bstack11ll1l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢቘ")
        bstack1ll11llllll_opy_ = result.get(bstack11ll1l_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣ቙"), TestFramework.bstack1ll11l1llll_opy_)
        if bstack1ll11llllll_opy_ != TestFramework.bstack1ll11l1llll_opy_:
            TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1ll1111l1ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11ll1lll_opy_(instance, {
            TestFramework.bstack1lll1l11l11_opy_: failure,
            TestFramework.bstack1ll1l11l1ll_opy_: bstack11111111ll_opy_,
            TestFramework.bstack1lll1l11111_opy_: bstack1ll11llllll_opy_,
        })
    def __1ll1l1l111l_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1lll1l1l11l_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1l11l_opy_.SETUP_FIXTURE:
            instance = self.__1ll1111ll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l11l1l1_opy_ bstack1ll11ll11l1_opy_ this to be bstack11ll1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣቚ")
            if test_framework_state == bstack1lll1l1l11l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11lllll1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1l11l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11ll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࠢቛ"), None), bstack11ll1l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥቜ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11ll1l_opy_ (u"ࠦࡳࡵࡤࡦࠤቝ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11ll1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ቞"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111l1l11_opy_(target) if target else None
        return instance
    def __1l1lllllll1_opy_(
        self,
        instance: bstack1lll1l11lll_opy_,
        test_framework_state: bstack1lll1l1l11l_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1111l11l_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll1l11l111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1llll1ll1_opy_, {})
        if not key in bstack1ll1l11l111_opy_:
            bstack1ll1l11l111_opy_[key] = []
        bstack1ll11l11l1l_opy_ = {
            PytestBDDFramework.bstack1ll1111l11l_opy_: bstack1l1llllll11_opy_,
            PytestBDDFramework.bstack1l1llll1ll1_opy_: bstack1ll1l11l111_opy_,
        }
        if test_hook_state == bstack1lll11lll1l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11ll1l_opy_ (u"ࠨ࡫ࡦࡻࠥ቟"): key,
                TestFramework.bstack1ll11l1l111_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l1ll1l_opy_: TestFramework.bstack1l1llll1l11_opy_,
                TestFramework.bstack1ll11llll1l_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll111l1ll1_opy_: [],
                TestFramework.bstack1l1llll1111_opy_: hook_name,
                TestFramework.bstack1l1llll11l1_opy_: bstack1ll1l1l1l11_opy_.bstack1ll11ll11ll_opy_()
            }
            bstack1l1llllll11_opy_[key].append(hook)
            bstack1ll11l11l1l_opy_[PytestBDDFramework.bstack1ll1l11lll1_opy_] = key
        elif test_hook_state == bstack1lll11lll1l_opy_.POST:
            bstack1ll11l111l1_opy_ = bstack1l1llllll11_opy_.get(key, [])
            hook = bstack1ll11l111l1_opy_.pop() if bstack1ll11l111l1_opy_ else None
            if hook:
                result = self.__1ll1111111l_opy_(*args)
                if result:
                    bstack1ll1111l1l1_opy_ = result.get(bstack11ll1l_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣበ"), TestFramework.bstack1l1llll1l11_opy_)
                    if bstack1ll1111l1l1_opy_ != TestFramework.bstack1l1llll1l11_opy_:
                        hook[TestFramework.bstack1ll11l1ll1l_opy_] = bstack1ll1111l1l1_opy_
                hook[TestFramework.bstack1ll1l11ll1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1l1llll11l1_opy_] = bstack1ll1l1l1l11_opy_.bstack1ll11ll11ll_opy_()
                self.bstack1ll11lll1l1_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11ll1ll1_opy_, [])
                self.bstack1ll111lllll_opy_(instance, logs)
                bstack1ll1l11l111_opy_[key].append(hook)
                bstack1ll11l11l1l_opy_[PytestBDDFramework.bstack1ll1l11ll11_opy_] = key
        TestFramework.bstack1ll11ll1lll_opy_(instance, bstack1ll11l11l1l_opy_)
        self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡩࡱࡲ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼ࡭ࡨࡽࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࡀࡿ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࢁࠥ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡃࠢቡ") + str(bstack1ll1l11l111_opy_) + bstack11ll1l_opy_ (u"ࠤࠥቢ"))
    def __1ll1111ll1l_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1lll1l1l11l_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111llll1_opy_(args[0], [bstack11ll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤባ"), bstack11ll1l_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧቤ"), bstack11ll1l_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧብ"), bstack11ll1l_opy_ (u"ࠨࡩࡥࡵࠥቦ"), bstack11ll1l_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤቧ"), bstack11ll1l_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣቨ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11ll1l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣቩ")) else fixturedef.get(bstack11ll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤቪ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11ll1l_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࠤቫ")) else None
        node = request.node if hasattr(request, bstack11ll1l_opy_ (u"ࠧࡴ࡯ࡥࡧࠥቬ")) else None
        target = request.node.nodeid if hasattr(node, bstack11ll1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨቭ")) else None
        baseid = fixturedef.get(bstack11ll1l_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢቮ"), None) or bstack11ll1l_opy_ (u"ࠣࠤቯ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11ll1l_opy_ (u"ࠤࡢࡴࡾ࡬ࡵ࡯ࡥ࡬ࡸࡪࡳࠢተ")):
            target = PytestBDDFramework.__1ll1l111lll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11ll1l_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧቱ")) else None
            if target and not TestFramework.bstack1ll111l1l11_opy_(target):
                self.__1ll11lllll1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦ࡮ࡰࡦࡨࡁࢀࡴ࡯ࡥࡧࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨቲ") + str(test_hook_state) + bstack11ll1l_opy_ (u"ࠧࠨታ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦቴ") + str(target) + bstack11ll1l_opy_ (u"ࠢࠣት"))
            return None
        instance = TestFramework.bstack1ll111l1l11_opy_(target)
        if not instance:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡣࡣࡶࡩ࡮ࡪ࠽ࡼࡤࡤࡷࡪ࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥቶ") + str(target) + bstack11ll1l_opy_ (u"ࠤࠥቷ"))
            return None
        bstack1ll11l11ll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l11111l_opy_, {})
        if os.getenv(bstack11ll1l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡉࡍ࡝࡚ࡕࡓࡇࡖࠦቸ"), bstack11ll1l_opy_ (u"ࠦ࠶ࠨቹ")) == bstack11ll1l_opy_ (u"ࠧ࠷ࠢቺ"):
            bstack1ll11llll11_opy_ = bstack11ll1l_opy_ (u"ࠨ࠺ࠣቻ").join((scope, fixturename))
            bstack1ll1l11l11l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11l1l1l1_opy_ = {
                bstack11ll1l_opy_ (u"ࠢ࡬ࡧࡼࠦቼ"): bstack1ll11llll11_opy_,
                bstack11ll1l_opy_ (u"ࠣࡶࡤ࡫ࡸࠨች"): PytestBDDFramework.__1ll111l1lll_opy_(request.node, scenario),
                bstack11ll1l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࠥቾ"): fixturedef,
                bstack11ll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤቿ"): scope,
                bstack11ll1l_opy_ (u"ࠦࡹࡿࡰࡦࠤኀ"): None,
            }
            try:
                if test_hook_state == bstack1lll11lll1l_opy_.POST and callable(getattr(args[-1], bstack11ll1l_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤኁ"), None)):
                    bstack1ll11l1l1l1_opy_[bstack11ll1l_opy_ (u"ࠨࡴࡺࡲࡨࠦኂ")] = TestFramework.bstack1l1llll1l1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll11l1l1l1_opy_[bstack11ll1l_opy_ (u"ࠢࡶࡷ࡬ࡨࠧኃ")] = uuid4().__str__()
                bstack1ll11l1l1l1_opy_[PytestBDDFramework.bstack1ll11llll1l_opy_] = bstack1ll1l11l11l_opy_
            elif test_hook_state == bstack1lll11lll1l_opy_.POST:
                bstack1ll11l1l1l1_opy_[PytestBDDFramework.bstack1ll1l11ll1l_opy_] = bstack1ll1l11l11l_opy_
            if bstack1ll11llll11_opy_ in bstack1ll11l11ll1_opy_:
                bstack1ll11l11ll1_opy_[bstack1ll11llll11_opy_].update(bstack1ll11l1l1l1_opy_)
                self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࠾ࠤኄ") + str(bstack1ll11l11ll1_opy_[bstack1ll11llll11_opy_]) + bstack11ll1l_opy_ (u"ࠤࠥኅ"))
            else:
                bstack1ll11l11ll1_opy_[bstack1ll11llll11_opy_] = bstack1ll11l1l1l1_opy_
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡾࠢࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࠨኆ") + str(len(bstack1ll11l11ll1_opy_)) + bstack11ll1l_opy_ (u"ࠦࠧኇ"))
        TestFramework.bstack1llll1l1lll_opy_(instance, PytestBDDFramework.bstack1ll1l11111l_opy_, bstack1ll11l11ll1_opy_)
        self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࡻ࡭ࡧࡱࠬࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠩࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧኈ") + str(instance.ref()) + bstack11ll1l_opy_ (u"ࠨࠢ኉"))
        return instance
    def __1ll11lllll1_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1lll1l1l11l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        ob = bstack1lll1l11lll_opy_(ctx, self.bstack1ll111l11l1_opy_, self.bstack1ll11ll1111_opy_, test_framework_state)
        TestFramework.bstack1ll11ll1lll_opy_(ob, {
            TestFramework.bstack1llll111l11_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1lll1_opy_: context.test_framework_version,
            TestFramework.bstack1ll11ll111l_opy_: [],
            PytestBDDFramework.bstack1ll1l11111l_opy_: {},
            PytestBDDFramework.bstack1l1llll1ll1_opy_: {},
            PytestBDDFramework.bstack1ll1111l11l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l1lll_opy_(ob, TestFramework.bstack1ll1111lll1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l1lll_opy_(ob, TestFramework.bstack1lllll1llll_opy_, context.platform_index)
        TestFramework.bstack1lll1l1ll1l_opy_[ctx.id] = ob
        self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡥࡷࡼ࠳࡯ࡤ࠾ࡽࡦࡸࡽ࠴ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢኊ") + str(TestFramework.bstack1lll1l1ll1l_opy_.keys()) + bstack11ll1l_opy_ (u"ࠣࠤኋ"))
        return ob
    @staticmethod
    def __1ll11lll1ll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬኌ"): id(step),
                bstack11ll1l_opy_ (u"ࠪࡸࡪࡾࡴࠨኍ"): step.name,
                bstack11ll1l_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬ኎"): step.keyword,
            })
        meta = {
            bstack11ll1l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪ࠭኏"): {
                bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫነ"): feature.name,
                bstack11ll1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬኑ"): feature.filename,
                bstack11ll1l_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ኒ"): feature.description
            },
            bstack11ll1l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫና"): {
                bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨኔ"): scenario.name
            },
            bstack11ll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪን"): steps,
            bstack11ll1l_opy_ (u"ࠬ࡫ࡸࡢ࡯ࡳࡰࡪࡹࠧኖ"): PytestBDDFramework.__1ll111lll11_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll1l11llll_opy_: meta
            }
        )
    def bstack1ll11lll1l1_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡷࡵࡣࡦࡵࡶࡩࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡸ࡯࡭ࡪ࡮ࡤࡶࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡡࡷࡣࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩ࡫ࡶࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡇ࡭࡫ࡣ࡬ࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡩ࡯ࡵ࡬ࡨࡪࠦࡾ࠰࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠰ࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡆࡰࡴࠣࡩࡦࡩࡨࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠱ࠦࡲࡦࡲ࡯ࡥࡨ࡫ࡳࠡࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧࠦࡷࡪࡶ࡫ࠤࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣࠢ࡬ࡲࠥ࡯ࡴࡴࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡉࡧࠢࡤࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡺࡨࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡳࡡࡵࡥ࡫ࡩࡸࠦࡡࠡ࡯ࡲࡨ࡮࡬ࡩࡦࡦࠣ࡬ࡴࡵ࡫࠮࡮ࡨࡺࡪࡲࠠࡧ࡫࡯ࡩ࠱ࠦࡩࡵࠢࡦࡶࡪࡧࡴࡦࡵࠣࡥࠥࡒ࡯ࡨࡇࡱࡸࡷࡿࠠࡰࡤ࡭ࡩࡨࡺࠠࡸ࡫ࡷ࡬ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡧࡩࡹࡧࡩ࡭ࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡖ࡭ࡲ࡯࡬ࡢࡴ࡯ࡽ࠱ࠦࡩࡵࠢࡳࡶࡴࡩࡥࡴࡵࡨࡷࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠ࡭ࡱࡦࡥࡹ࡫ࡤࠡ࡫ࡱࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡢࡺࠢࡵࡩࡵࡲࡡࡤ࡫ࡱ࡫ࠥࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡚ࠥࡨࡦࠢࡦࡶࡪࡧࡴࡦࡦࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡡࡳࡧࠣࡥࡩࡪࡥࡥࠢࡷࡳࠥࡺࡨࡦࠢ࡫ࡳࡴࡱࠧࡴࠢࠥࡰࡴ࡭ࡳࠣࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮࠾࡚ࠥࡨࡦࠢࡨࡺࡪࡴࡴࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡱࡵࡧࡴࠢࡤࡲࡩࠦࡨࡰࡱ࡮ࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠣࡱࡴࡴࡩࡵࡱࡵ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡱࡴࡴࡩࡵࡱࡵ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧኗ")
        global _1l1llllllll_opy_
        platform_index = os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧኘ")]
        bstack1l1llll11ll_opy_ = os.path.join(bstack1ll1111l111_opy_, (bstack1l1llll1lll_opy_ + str(platform_index)), bstack1ll11l11l11_opy_)
        if not os.path.exists(bstack1l1llll11ll_opy_) or not os.path.isdir(bstack1l1llll11ll_opy_):
            return
        logs = hook.get(bstack11ll1l_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨኙ"), [])
        with os.scandir(bstack1l1llll11ll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1l1llllllll_opy_:
                    self.logger.info(bstack11ll1l_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢኚ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11ll1l_opy_ (u"ࠥࠦኛ")
                    log_entry = bstack1ll11lll11l_opy_(
                        kind=bstack11ll1l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨኜ"),
                        message=bstack11ll1l_opy_ (u"ࠧࠨኝ"),
                        level=bstack11ll1l_opy_ (u"ࠨࠢኞ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll111ll1ll_opy_=entry.stat().st_size,
                        bstack1ll111lll1l_opy_=bstack11ll1l_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢኟ"),
                        bstack1l1ll_opy_=os.path.abspath(entry.path),
                        bstack1l1llllll1l_opy_=hook.get(TestFramework.bstack1ll11l1l111_opy_)
                    )
                    logs.append(log_entry)
                    _1l1llllllll_opy_.add(abs_path)
        platform_index = os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨአ")]
        bstack1ll1l111l1l_opy_ = os.path.join(bstack1ll1111l111_opy_, (bstack1l1llll1lll_opy_ + str(platform_index)), bstack1ll11l11l11_opy_, bstack1ll1l1111ll_opy_)
        if not os.path.exists(bstack1ll1l111l1l_opy_) or not os.path.isdir(bstack1ll1l111l1l_opy_):
            self.logger.info(bstack11ll1l_opy_ (u"ࠤࡑࡳࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡬࡯ࡶࡰࡧࠤࡦࡺ࠺ࠡࡽࢀࠦኡ").format(bstack1ll1l111l1l_opy_))
        else:
            self.logger.info(bstack11ll1l_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤኢ").format(bstack1ll1l111l1l_opy_))
            with os.scandir(bstack1ll1l111l1l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1l1llllllll_opy_:
                        self.logger.info(bstack11ll1l_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤኣ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11ll1l_opy_ (u"ࠧࠨኤ")
                        log_entry = bstack1ll11lll11l_opy_(
                            kind=bstack11ll1l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣእ"),
                            message=bstack11ll1l_opy_ (u"ࠢࠣኦ"),
                            level=bstack11ll1l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧኧ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll111ll1ll_opy_=entry.stat().st_size,
                            bstack1ll111lll1l_opy_=bstack11ll1l_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤከ"),
                            bstack1l1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll1l111l11_opy_=hook.get(TestFramework.bstack1ll11l1l111_opy_)
                        )
                        logs.append(log_entry)
                        _1l1llllllll_opy_.add(abs_path)
        hook[bstack11ll1l_opy_ (u"ࠥࡰࡴ࡭ࡳࠣኩ")] = logs
    def bstack1ll111lllll_opy_(
        self,
        bstack1ll11l1l1ll_opy_: bstack1lll1l11lll_opy_,
        entries: List[bstack1ll11lll11l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣኪ"))
        req.platform_index = TestFramework.get_state(bstack1ll11l1l1ll_opy_, TestFramework.bstack1lllll1llll_opy_)
        req.execution_context.hash = str(bstack1ll11l1l1ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l1l1ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l1l1ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l1l1ll_opy_, TestFramework.bstack1llll111l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l1l1ll_opy_, TestFramework.bstack1lll1l1lll1_opy_)
            log_entry.uuid = entry.bstack1l1llllll1l_opy_ if entry.bstack1l1llllll1l_opy_ else TestFramework.get_state(bstack1ll11l1l1ll_opy_, TestFramework.bstack1lll1lllll1_opy_)
            log_entry.test_framework_state = bstack1ll11l1l1ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11ll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦካ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11ll1l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣኬ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111ll1ll_opy_
                log_entry.file_path = entry.bstack1l1ll_opy_
        def bstack1ll11l1lll1_opy_():
            bstack1ll11ll111_opy_ = datetime.now()
            try:
                self.bstack1lllll111l1_opy_.LogCreatedEvent(req)
                bstack1ll11l1l1ll_opy_.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦክ"), datetime.now() - bstack1ll11ll111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࢀࢃࠢኮ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l11l1_opy_.enqueue(bstack1ll11l1lll1_opy_)
    def __1ll1111ll11_opy_(self, instance) -> None:
        bstack11ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡌࡰࡣࡧࡷࠥࡩࡵࡴࡶࡲࡱࠥࡺࡡࡨࡵࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡵࡩࡦࡺࡥࡴࠢࡤࠤࡩ࡯ࡣࡵࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡱ࡫ࡶࡦ࡮ࠣࡧࡺࡹࡴࡰ࡯ࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡨࡵࡳࡲࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡷࡶࡸࡴࡳࡔࡢࡩࡐࡥࡳࡧࡧࡦࡴࠣࡥࡳࡪࠠࡶࡲࡧࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡴࡶࡤࡸࡪࠦࡵࡴ࡫ࡱ࡫ࠥࡹࡥࡵࡡࡶࡸࡦࡺࡥࡠࡧࡱࡸࡷ࡯ࡥࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢኯ")
        bstack1ll11l11l1l_opy_ = {bstack11ll1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧኰ"): bstack1ll1l1l1l11_opy_.bstack1ll11ll11ll_opy_()}
        TestFramework.bstack1ll11ll1lll_opy_(instance, bstack1ll11l11l1l_opy_)
    @staticmethod
    def __1l1lllll11l_opy_(instance, args):
        request, bstack1ll11111l11_opy_ = args
        bstack1l1lll1lll1_opy_ = id(bstack1ll11111l11_opy_)
        bstack1ll11l11lll_opy_ = instance.data[TestFramework.bstack1ll1l11llll_opy_]
        step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧ኱")] == bstack1l1lll1lll1_opy_, bstack1ll11l11lll_opy_[bstack11ll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኲ")]), None)
        step.update({
            bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪኳ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11l11lll_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኴ")]) if st[bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫኵ")] == step[bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ኶")]), None)
        if index is not None:
            bstack1ll11l11lll_opy_[bstack11ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ኷")][index] = step
        instance.data[TestFramework.bstack1ll1l11llll_opy_] = bstack1ll11l11lll_opy_
    @staticmethod
    def __1ll111111l1_opy_(instance, args):
        bstack11ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡫ࡩࡳࠦ࡬ࡦࡰࠣࡥࡷ࡭ࡳࠡ࡫ࡶࠤ࠷࠲ࠠࡪࡶࠣࡷ࡮࡭࡮ࡪࡨ࡬ࡩࡸࠦࡴࡩࡧࡵࡩࠥ࡯ࡳࠡࡰࡲࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡧࡲࡨࡵࠣࡥࡷ࡫ࠠ࠮ࠢ࡞ࡶࡪࡷࡵࡦࡵࡷ࠰ࠥࡹࡴࡦࡲࡠࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡࡣࡵ࡫ࡸࠦࡡࡳࡧࠣ࠷ࠥࡺࡨࡦࡰࠣࡸ࡭࡫ࠠ࡭ࡣࡶࡸࠥࡼࡡ࡭ࡷࡨࠤ࡮ࡹࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢኸ")
        bstack1ll111l1111_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll11111l11_opy_ = args[1]
        bstack1l1lll1lll1_opy_ = id(bstack1ll11111l11_opy_)
        bstack1ll11l11lll_opy_ = instance.data[TestFramework.bstack1ll1l11llll_opy_]
        step = None
        if bstack1l1lll1lll1_opy_ is not None and bstack1ll11l11lll_opy_.get(bstack11ll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኹ")):
            step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"࠭ࡩࡥࠩኺ")] == bstack1l1lll1lll1_opy_, bstack1ll11l11lll_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኻ")]), None)
            step.update({
                bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ኼ"): bstack1ll111l1111_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩኽ"): bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪኾ"),
                bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ኿"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬዀ"): bstack11ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭዁"),
                })
        index = next((i for i, st in enumerate(bstack1ll11l11lll_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ዂ")]) if st[bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫዃ")] == step[bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬዄ")]), None)
        if index is not None:
            bstack1ll11l11lll_opy_[bstack11ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩዅ")][index] = step
        instance.data[TestFramework.bstack1ll1l11llll_opy_] = bstack1ll11l11lll_opy_
    @staticmethod
    def __1ll111lll11_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11ll1l_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭዆")):
                examples = list(node.callspec.params[bstack11ll1l_opy_ (u"ࠬࡥࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡩࡽࡧ࡭ࡱ࡮ࡨࠫ዇")].values())
            return examples
        except:
            return []
    def bstack1l1lllll111_opy_(self, instance: bstack1lll1l11lll_opy_, bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll11l11111_opy_ = (
            PytestBDDFramework.bstack1ll1l11lll1_opy_
            if bstack1lllllllll1_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else PytestBDDFramework.bstack1ll1l11ll11_opy_
        )
        hook = PytestBDDFramework.bstack1ll1l1l1l1l_opy_(instance, bstack1ll11l11111_opy_)
        entries = hook.get(TestFramework.bstack1ll111l1ll1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11ll111l_opy_, []))
        return entries
    def bstack1l1lllll1l1_opy_(self, instance: bstack1lll1l11lll_opy_, bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll11l11111_opy_ = (
            PytestBDDFramework.bstack1ll1l11lll1_opy_
            if bstack1lllllllll1_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else PytestBDDFramework.bstack1ll1l11ll11_opy_
        )
        PytestBDDFramework.bstack1ll11111111_opy_(instance, bstack1ll11l11111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11ll111l_opy_, []).clear()
    @staticmethod
    def bstack1ll1l1l1l1l_opy_(instance: bstack1lll1l11lll_opy_, bstack1ll11l11111_opy_: str):
        bstack1l1lll1l11l_opy_ = (
            PytestBDDFramework.bstack1l1llll1ll1_opy_
            if bstack1ll11l11111_opy_ == PytestBDDFramework.bstack1ll1l11ll11_opy_
            else PytestBDDFramework.bstack1ll1111l11l_opy_
        )
        bstack1ll11ll1l11_opy_ = TestFramework.get_state(instance, bstack1ll11l11111_opy_, None)
        bstack1l1lll1l1l1_opy_ = TestFramework.get_state(instance, bstack1l1lll1l11l_opy_, None) if bstack1ll11ll1l11_opy_ else None
        return (
            bstack1l1lll1l1l1_opy_[bstack1ll11ll1l11_opy_][-1]
            if isinstance(bstack1l1lll1l1l1_opy_, dict) and len(bstack1l1lll1l1l1_opy_.get(bstack1ll11ll1l11_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11111111_opy_(instance: bstack1lll1l11lll_opy_, bstack1ll11l11111_opy_: str):
        hook = PytestBDDFramework.bstack1ll1l1l1l1l_opy_(instance, bstack1ll11l11111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll111l1ll1_opy_, []).clear()
    @staticmethod
    def __1ll1l1l1ll1_opy_(instance: bstack1lll1l11lll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11ll1l_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡩ࡯ࡳࡦࡶࠦወ"), None)):
            return
        if os.getenv(bstack11ll1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡌࡐࡉࡖࠦዉ"), bstack11ll1l_opy_ (u"ࠣ࠳ࠥዊ")) != bstack11ll1l_opy_ (u"ࠤ࠴ࠦዋ"):
            PytestBDDFramework.logger.warning(bstack11ll1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳ࡫ࡱ࡫ࠥࡩࡡࡱ࡮ࡲ࡫ࠧዌ"))
            return
        bstack1ll11lll111_opy_ = {
            bstack11ll1l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥው"): (PytestBDDFramework.bstack1ll1l11lll1_opy_, PytestBDDFramework.bstack1ll1111l11l_opy_),
            bstack11ll1l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢዎ"): (PytestBDDFramework.bstack1ll1l11ll11_opy_, PytestBDDFramework.bstack1l1llll1ll1_opy_),
        }
        for when in (bstack11ll1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧዏ"), bstack11ll1l_opy_ (u"ࠢࡤࡣ࡯ࡰࠧዐ"), bstack11ll1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥዑ")):
            bstack1ll111l11ll_opy_ = args[1].get_records(when)
            if not bstack1ll111l11ll_opy_:
                continue
            records = [
                bstack1ll11lll11l_opy_(
                    kind=TestFramework.bstack1l1llll111l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11ll1l_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩࠧዒ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11ll1l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡧࠦዓ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll111l11ll_opy_
                if isinstance(getattr(r, bstack11ll1l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧዔ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1l1l1111_opy_, bstack1l1lll1l11l_opy_ = bstack1ll11lll111_opy_.get(when, (None, None))
            bstack1ll11l1l11l_opy_ = TestFramework.get_state(instance, bstack1ll1l1l1111_opy_, None) if bstack1ll1l1l1111_opy_ else None
            bstack1l1lll1l1l1_opy_ = TestFramework.get_state(instance, bstack1l1lll1l11l_opy_, None) if bstack1ll11l1l11l_opy_ else None
            if isinstance(bstack1l1lll1l1l1_opy_, dict) and len(bstack1l1lll1l1l1_opy_.get(bstack1ll11l1l11l_opy_, [])) > 0:
                hook = bstack1l1lll1l1l1_opy_[bstack1ll11l1l11l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll111l1ll1_opy_ in hook:
                    hook[TestFramework.bstack1ll111l1ll1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11ll111l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11111lll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll11111ll1_opy_(request.node, scenario)
        bstack1ll1111llll_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll1111llll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1lllll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11l1111l_opy_: test_id,
            TestFramework.bstack1ll11111l1l_opy_: test_name,
            TestFramework.bstack1l1lll1llll_opy_: test_id,
            TestFramework.bstack1ll1l1111l1_opy_: bstack1ll1111llll_opy_,
            TestFramework.bstack1ll111111ll_opy_: PytestBDDFramework.__1ll111l1lll_opy_(feature, scenario),
            TestFramework.bstack1l1lll1ll11_opy_: code,
            TestFramework.bstack1lll1l11111_opy_: TestFramework.bstack1ll11l1llll_opy_,
            TestFramework.bstack1ll1llllll1_opy_: test_name
        }
    @staticmethod
    def __1ll11111ll1_opy_(node, scenario):
        if hasattr(node, bstack11ll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧዕ")):
            parts = node.nodeid.rsplit(bstack11ll1l_opy_ (u"ࠨ࡛ࠣዖ"))
            params = parts[-1]
            return bstack11ll1l_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢ዗").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll111l1lll_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11ll1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ዘ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11ll1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧዙ")) else [])
    @staticmethod
    def __1ll1l111lll_opy_(location):
        return bstack11ll1l_opy_ (u"ࠥ࠾࠿ࠨዚ").join(filter(lambda x: isinstance(x, str), location))