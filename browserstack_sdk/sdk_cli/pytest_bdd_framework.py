# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1ll1ll11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l11l1l_opy_ import bstack1ll1l111111_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll1lll_opy_,
    bstack1lll1l1ll1l_opy_,
    bstack1lll11lll1l_opy_,
    bstack1ll1111ll1l_opy_,
    bstack1ll11ll1l1l_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l1ll111_opy_
from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll111l1l1l_opy_ import bstack1ll11111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
bstack1ll1l1l1l1l_opy_ = bstack1ll1l1ll111_opy_()
bstack1ll111ll111_opy_ = bstack11l111_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣማ")
bstack1ll11l1l1ll_opy_ = bstack11l111_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧሜ")
bstack1ll1l1l1lll_opy_ = bstack11l111_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤም")
bstack1ll11lll11l_opy_ = 1.0
_1ll1l1l1l11_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll111lllll_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦሞ")
    bstack1l1lllllll1_opy_ = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࠥሟ")
    bstack1ll11ll1lll_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧሠ")
    bstack1ll111l1ll1_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࠤሡ")
    bstack1ll111l111l_opy_ = bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦሢ")
    bstack1ll1l11llll_opy_: bool
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_  = None
    bstack1l1lll1lll1_opy_ = [
        bstack1lll1ll1lll_opy_.BEFORE_ALL,
        bstack1lll1ll1lll_opy_.AFTER_ALL,
        bstack1lll1ll1lll_opy_.BEFORE_EACH,
        bstack1lll1ll1lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111ll1l1_opy_: Dict[str, str],
        bstack1ll111111ll_opy_: List[str]=[bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨሣ")],
        bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_ = None,
        bstack1llllll1l11_opy_=None
    ):
        super().__init__(bstack1ll111111ll_opy_, bstack1ll111ll1l1_opy_, bstack1lll11l1l1l_opy_)
        self.bstack1ll1l11llll_opy_ = any(bstack11l111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢሤ") in item.lower() for item in bstack1ll111111ll_opy_)
        self.bstack1llllll1l11_opy_ = bstack1llllll1l11_opy_
    def track_event(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll1lll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1l1lll1lll1_opy_:
            bstack1ll1l111111_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll1lll_opy_.NONE:
            self.logger.warning(bstack11l111_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨࡨࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࠧሥ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠧࠨሦ"))
            return
        if not self.bstack1ll1l11llll_opy_:
            self.logger.warning(bstack11l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡃࠢሧ") + str(str(self.bstack1ll111111ll_opy_)) + bstack11l111_opy_ (u"ࠢࠣረ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥሩ") + str(kwargs) + bstack11l111_opy_ (u"ࠤࠥሪ"))
            return
        instance = self.__1l1llllll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡥࡷ࡭ࡳ࠾ࠤራ") + str(args) + bstack11l111_opy_ (u"ࠦࠧሬ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1lll1lll1_opy_ and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack1l1ll1111_opy_.value)
                name = str(EVENTS.bstack1l1ll1111_opy_.name)+bstack11l111_opy_ (u"ࠧࡀࠢር")+str(test_framework_state.name)
                TestFramework.bstack1ll11111lll_opy_(instance, name, bstack1ll1l1l11l1_opy_)
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳࠢࡳࡶࡪࡀࠠࡼࡿࠥሮ").format(e))
        try:
            if test_framework_state == bstack1lll1ll1lll_opy_.TEST:
                if not TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_) and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll111ll11l_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11l111_opy_ (u"ࠢ࡭ࡱࡤࡨࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢሯ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠣࠤሰ"))
                if test_hook_state == bstack1lll11lll1l_opy_.PRE and not TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1ll1l111lll_opy_):
                    TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll1l111lll_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1l11ll1l_opy_(instance, args)
                    self.logger.debug(bstack11l111_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡸࡺࡡࡳࡶࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢሱ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠥࠦሲ"))
                elif test_hook_state == bstack1lll11lll1l_opy_.POST and not TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1ll11ll111l_opy_):
                    TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll11ll111l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l111_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡥ࡯ࡦࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢሳ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠧࠨሴ"))
            elif test_framework_state == bstack1lll1ll1lll_opy_.STEP:
                if test_hook_state == bstack1lll11lll1l_opy_.PRE:
                    PytestBDDFramework.__1l1llllll11_opy_(instance, args)
                elif test_hook_state == bstack1lll11lll1l_opy_.POST:
                    PytestBDDFramework.__1ll111l11ll_opy_(instance, args)
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG and test_hook_state == bstack1lll11lll1l_opy_.POST:
                PytestBDDFramework.__1ll1111111l_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG_REPORT and test_hook_state == bstack1lll11lll1l_opy_.POST:
                self.__1l1llll1l1l_opy_(instance, *args)
                self.__1ll1111l1l1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1l1lll1lll1_opy_:
                self.__1ll1111l1ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢስ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠢࠣሶ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l1111l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1lll1lll1_opy_ and test_hook_state == bstack1lll11lll1l_opy_.POST:
                name = str(EVENTS.bstack1l1ll1111_opy_.name)+bstack11l111_opy_ (u"ࠣ࠼ࠥሷ")+str(test_framework_state.name)
                bstack1ll1l1l11l1_opy_ = TestFramework.bstack1ll1l111l11_opy_(instance, name)
                bstack1llll11ll11_opy_.end(EVENTS.bstack1l1ll1111_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤሸ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣሹ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦሺ").format(e))
    def bstack1ll1l11ll11_opy_(self):
        return self.bstack1ll1l11llll_opy_
    def __1ll1l1l1ll1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l111_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤሻ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11llll1l_opy_(rep, [bstack11l111_opy_ (u"ࠨࡷࡩࡧࡱࠦሼ"), bstack11l111_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣሽ"), bstack11l111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣሾ"), bstack11l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤሿ"), bstack11l111_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠦቀ"), bstack11l111_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥቁ")])
        return None
    def __1l1llll1l1l_opy_(self, instance: bstack1lll1l1ll1l_opy_, *args):
        result = self.__1ll1l1l1ll1_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111lll_opy_ = None
        if result.get(bstack11l111_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨቂ"), None) == bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨቃ") and len(args) > 1 and getattr(args[1], bstack11l111_opy_ (u"ࠢࡦࡺࡦ࡭ࡳ࡬࡯ࠣቄ"), None) is not None:
            failure = [{bstack11l111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫቅ"): [args[1].excinfo.exconly(), result.get(bstack11l111_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣቆ"), None)]}]
            bstack1111111lll_opy_ = bstack11l111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦቇ") if bstack11l111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢቈ") in getattr(args[1].excinfo, bstack11l111_opy_ (u"ࠧࡺࡹࡱࡧࡱࡥࡲ࡫ࠢ቉"), bstack11l111_opy_ (u"ࠨࠢቊ")) else bstack11l111_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣቋ")
        bstack1ll11llll11_opy_ = result.get(bstack11l111_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤቌ"), TestFramework.bstack1ll1l11lll1_opy_)
        if bstack1ll11llll11_opy_ != TestFramework.bstack1ll1l11lll1_opy_:
            TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11l11l11_opy_(instance, {
            TestFramework.bstack1lll1ll1ll1_opy_: failure,
            TestFramework.bstack1ll11l11111_opy_: bstack1111111lll_opy_,
            TestFramework.bstack1llll1111l1_opy_: bstack1ll11llll11_opy_,
        })
    def __1l1llllll1l_opy_(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll1lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11l1ll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l11l1ll_opy_ bstack1l1llll1111_opy_ this to be bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤቍ")
            if test_framework_state == bstack1lll1ll1lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11l1llll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l111_opy_ (u"ࠥࡲࡴࡪࡥࠣ቎"), None), bstack11l111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦ቏"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l111_opy_ (u"ࠧࡴ࡯ࡥࡧࠥቐ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11l111_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨቑ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111lll1l_opy_(target) if target else None
        return instance
    def __1ll1111l1ll_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1111l11l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1lllllll1_opy_, {})
        if not key in bstack1ll1111l11l_opy_:
            bstack1ll1111l11l_opy_[key] = []
        bstack1ll11lll1l1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll1lll_opy_, {})
        if not key in bstack1ll11lll1l1_opy_:
            bstack1ll11lll1l1_opy_[key] = []
        bstack1ll11111ll1_opy_ = {
            PytestBDDFramework.bstack1l1lllllll1_opy_: bstack1ll1111l11l_opy_,
            PytestBDDFramework.bstack1ll11ll1lll_opy_: bstack1ll11lll1l1_opy_,
        }
        if test_hook_state == bstack1lll11lll1l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11l111_opy_ (u"ࠢ࡬ࡧࡼࠦቒ"): key,
                TestFramework.bstack1ll11l11l1l_opy_: uuid4().__str__(),
                TestFramework.bstack1ll111l1111_opy_: TestFramework.bstack1ll111lll11_opy_,
                TestFramework.bstack1l1lllll1ll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l111l1_opy_: [],
                TestFramework.bstack1ll11llllll_opy_: hook_name,
                TestFramework.bstack1ll11lllll1_opy_: bstack1ll11111l1l_opy_.bstack1l1lll1llll_opy_()
            }
            bstack1ll1111l11l_opy_[key].append(hook)
            bstack1ll11111ll1_opy_[PytestBDDFramework.bstack1ll111l1ll1_opy_] = key
        elif test_hook_state == bstack1lll11lll1l_opy_.POST:
            bstack1ll11111111_opy_ = bstack1ll1111l11l_opy_.get(key, [])
            hook = bstack1ll11111111_opy_.pop() if bstack1ll11111111_opy_ else None
            if hook:
                result = self.__1ll1l1l1ll1_opy_(*args)
                if result:
                    bstack1l1lll1ll11_opy_ = result.get(bstack11l111_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤቓ"), TestFramework.bstack1ll111lll11_opy_)
                    if bstack1l1lll1ll11_opy_ != TestFramework.bstack1ll111lll11_opy_:
                        hook[TestFramework.bstack1ll111l1111_opy_] = bstack1l1lll1ll11_opy_
                hook[TestFramework.bstack1ll11l1lll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11lllll1_opy_] = bstack1ll11111l1l_opy_.bstack1l1lll1llll_opy_()
                self.bstack1l1llll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1l1lllll11l_opy_, [])
                self.bstack1l1llll11ll_opy_(instance, logs)
                bstack1ll11lll1l1_opy_[key].append(hook)
                bstack1ll11111ll1_opy_[PytestBDDFramework.bstack1ll111l111l_opy_] = key
        TestFramework.bstack1ll11l11l11_opy_(instance, bstack1ll11111ll1_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡪࡲࡳࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽ࡮ࡩࡾࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࡁࢀ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࢂࠦࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࠽ࠣቔ") + str(bstack1ll11lll1l1_opy_) + bstack11l111_opy_ (u"ࠥࠦቕ"))
    def __1ll11l1ll1l_opy_(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11llll1l_opy_(args[0], [bstack11l111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥቖ"), bstack11l111_opy_ (u"ࠧࡧࡲࡨࡰࡤࡱࡪࠨ቗"), bstack11l111_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨቘ"), bstack11l111_opy_ (u"ࠢࡪࡦࡶࠦ቙"), bstack11l111_opy_ (u"ࠣࡷࡱ࡭ࡹࡺࡥࡴࡶࠥቚ"), bstack11l111_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤቛ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11l111_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤቜ")) else fixturedef.get(bstack11l111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥቝ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l111_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥ቞")) else None
        node = request.node if hasattr(request, bstack11l111_opy_ (u"ࠨ࡮ࡰࡦࡨࠦ቟")) else None
        target = request.node.nodeid if hasattr(node, bstack11l111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢበ")) else None
        baseid = fixturedef.get(bstack11l111_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣቡ"), None) or bstack11l111_opy_ (u"ࠤࠥቢ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l111_opy_ (u"ࠥࡣࡵࡿࡦࡶࡰࡦ࡭ࡹ࡫࡭ࠣባ")):
            target = PytestBDDFramework.__1ll11ll1111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l111_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨቤ")) else None
            if target and not TestFramework.bstack1ll111lll1l_opy_(target):
                self.__1ll11l1llll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠ࡯ࡱࡧࡩࡂࢁ࡮ࡰࡦࡨࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢብ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠨࠢቦ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࡂࢁࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧቧ") + str(target) + bstack11l111_opy_ (u"ࠣࠤቨ"))
            return None
        instance = TestFramework.bstack1ll111lll1l_opy_(target)
        if not instance:
            self.logger.warning(bstack11l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡤࡤࡷࡪ࡯ࡤ࠾ࡽࡥࡥࡸ࡫ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦቩ") + str(target) + bstack11l111_opy_ (u"ࠥࠦቪ"))
            return None
        bstack1ll1111l111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111lllll_opy_, {})
        if os.getenv(bstack11l111_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡊࡎ࡞ࡔࡖࡔࡈࡗࠧቫ"), bstack11l111_opy_ (u"ࠧ࠷ࠢቬ")) == bstack11l111_opy_ (u"ࠨ࠱ࠣቭ"):
            bstack1ll11ll11l1_opy_ = bstack11l111_opy_ (u"ࠢ࠻ࠤቮ").join((scope, fixturename))
            bstack1l1lll1ll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11ll11ll_opy_ = {
                bstack11l111_opy_ (u"ࠣ࡭ࡨࡽࠧቯ"): bstack1ll11ll11l1_opy_,
                bstack11l111_opy_ (u"ࠤࡷࡥ࡬ࡹࠢተ"): PytestBDDFramework.__1ll11l1l11l_opy_(request.node, scenario),
                bstack11l111_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࠦቱ"): fixturedef,
                bstack11l111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥቲ"): scope,
                bstack11l111_opy_ (u"ࠧࡺࡹࡱࡧࠥታ"): None,
            }
            try:
                if test_hook_state == bstack1lll11lll1l_opy_.POST and callable(getattr(args[-1], bstack11l111_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥቴ"), None)):
                    bstack1ll11ll11ll_opy_[bstack11l111_opy_ (u"ࠢࡵࡻࡳࡩࠧት")] = TestFramework.bstack1ll111111l1_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll11ll11ll_opy_[bstack11l111_opy_ (u"ࠣࡷࡸ࡭ࡩࠨቶ")] = uuid4().__str__()
                bstack1ll11ll11ll_opy_[PytestBDDFramework.bstack1l1lllll1ll_opy_] = bstack1l1lll1ll1l_opy_
            elif test_hook_state == bstack1lll11lll1l_opy_.POST:
                bstack1ll11ll11ll_opy_[PytestBDDFramework.bstack1ll11l1lll1_opy_] = bstack1l1lll1ll1l_opy_
            if bstack1ll11ll11l1_opy_ in bstack1ll1111l111_opy_:
                bstack1ll1111l111_opy_[bstack1ll11ll11l1_opy_].update(bstack1ll11ll11ll_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࠥቷ") + str(bstack1ll1111l111_opy_[bstack1ll11ll11l1_opy_]) + bstack11l111_opy_ (u"ࠥࠦቸ"))
            else:
                bstack1ll1111l111_opy_[bstack1ll11ll11l1_opy_] = bstack1ll11ll11ll_opy_
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࡾࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡿࠣࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࠢቹ") + str(len(bstack1ll1111l111_opy_)) + bstack11l111_opy_ (u"ࠧࠨቺ"))
        TestFramework.bstack1llllllll1l_opy_(instance, PytestBDDFramework.bstack1ll111lllll_opy_, bstack1ll1111l111_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࡼ࡮ࡨࡲ࠭ࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠪࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨቻ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠢࠣቼ"))
        return instance
    def __1ll11l1llll_opy_(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        ob = bstack1lll1l1ll1l_opy_(ctx, self.bstack1ll111111ll_opy_, self.bstack1ll111ll1l1_opy_, test_framework_state)
        TestFramework.bstack1ll11l11l11_opy_(ob, {
            TestFramework.bstack1lll1l11l11_opy_: context.test_framework_name,
            TestFramework.bstack1lll11ll111_opy_: context.test_framework_version,
            TestFramework.bstack1ll11ll1ll1_opy_: [],
            PytestBDDFramework.bstack1ll111lllll_opy_: {},
            PytestBDDFramework.bstack1ll11ll1lll_opy_: {},
            PytestBDDFramework.bstack1l1lllllll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llllllll1l_opy_(ob, TestFramework.bstack1ll11l1l111_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llllllll1l_opy_(ob, TestFramework.bstack1llllllll11_opy_, context.platform_index)
        TestFramework.bstack1lll11llll1_opy_[ctx.id] = ob
        self.logger.debug(bstack11l111_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡦࡸࡽ࠴ࡩࡥ࠿ࡾࡧࡹࡾ࠮ࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣች") + str(TestFramework.bstack1lll11llll1_opy_.keys()) + bstack11l111_opy_ (u"ࠤࠥቾ"))
        return ob
    @staticmethod
    def __1ll1l11ll1l_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭ቿ"): id(step),
                bstack11l111_opy_ (u"ࠫࡹ࡫ࡸࡵࠩኀ"): step.name,
                bstack11l111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ኁ"): step.keyword,
            })
        meta = {
            bstack11l111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧኂ"): {
                bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬኃ"): feature.name,
                bstack11l111_opy_ (u"ࠨࡲࡤࡸ࡭࠭ኄ"): feature.filename,
                bstack11l111_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧኅ"): feature.description
            },
            bstack11l111_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬኆ"): {
                bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩኇ"): scenario.name
            },
            bstack11l111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኈ"): steps,
            bstack11l111_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨ኉"): PytestBDDFramework.__1ll111ll1ll_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll11lll1ll_opy_: meta
            }
        )
    def bstack1l1llll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡹࡩ࡮࡫࡯ࡥࡷࠦࡴࡰࠢࡷ࡬ࡪࠦࡊࡢࡸࡤࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪ࡬ࡷࠥࡳࡥࡵࡪࡲࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡈ࡮ࡥࡤ࡭ࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡇࡱࡵࠤࡪࡧࡣࡩࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸ࠲ࠠࡳࡧࡳࡰࡦࡩࡥࡴࠢࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤࠣ࡭ࡳࠦࡩࡵࡵࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡊࡨࠣࡥࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡩࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡭ࡢࡶࡦ࡬ࡪࡹࠠࡢࠢࡰࡳࡩ࡯ࡦࡪࡧࡧࠤ࡭ࡵ࡯࡬࠯࡯ࡩࡻ࡫࡬ࠡࡨ࡬ࡰࡪ࠲ࠠࡪࡶࠣࡧࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࠡࡹ࡬ࡸ࡭ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡗ࡮ࡳࡩ࡭ࡣࡵࡰࡾ࠲ࠠࡪࡶࠣࡴࡷࡵࡣࡦࡵࡶࡩࡸࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡ࡮ࡲࡧࡦࡺࡥࡥࠢ࡬ࡲࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡣࡻࠣࡶࡪࡶ࡬ࡢࡥ࡬ࡲ࡬ࠦࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡔࡩࡧࠣࡧࡷ࡫ࡡࡵࡧࡧࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡢࡴࡨࠤࡦࡪࡤࡦࡦࠣࡸࡴࠦࡴࡩࡧࠣ࡬ࡴࡵ࡫ࠨࡵࠣࠦࡱࡵࡧࡴࠤࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯࠿ࠦࡔࡩࡧࠣࡩࡻ࡫࡮ࡵࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵࠣࡥࡳࡪࠠࡩࡱࡲ࡯ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨኊ")
        global _1ll1l1l1l11_opy_
        platform_index = os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨኋ")]
        bstack1ll1l1l111l_opy_ = os.path.join(bstack1ll1l1l1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack1ll11l1l1ll_opy_)
        if not os.path.exists(bstack1ll1l1l111l_opy_) or not os.path.isdir(bstack1ll1l1l111l_opy_):
            return
        logs = hook.get(bstack11l111_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢኌ"), [])
        with os.scandir(bstack1ll1l1l111l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l1l1l11_opy_:
                    self.logger.info(bstack11l111_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣኍ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l111_opy_ (u"ࠦࠧ኎")
                    log_entry = bstack1ll11ll1l1l_opy_(
                        kind=bstack11l111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢ኏"),
                        message=bstack11l111_opy_ (u"ࠨࠢነ"),
                        level=bstack11l111_opy_ (u"ࠢࠣኑ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1llll11l1_opy_=entry.stat().st_size,
                        bstack1ll1111lll1_opy_=bstack11l111_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣኒ"),
                        bstack11ll1ll_opy_=os.path.abspath(entry.path),
                        bstack1ll1111llll_opy_=hook.get(TestFramework.bstack1ll11l11l1l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l1l1l11_opy_.add(abs_path)
        platform_index = os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩና")]
        bstack1ll1l111ll1_opy_ = os.path.join(bstack1ll1l1l1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack1ll11l1l1ll_opy_, bstack1ll1l1l1lll_opy_)
        if not os.path.exists(bstack1ll1l111ll1_opy_) or not os.path.isdir(bstack1ll1l111ll1_opy_):
            self.logger.info(bstack11l111_opy_ (u"ࠥࡒࡴࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡦࡰࡷࡱࡨࠥࡧࡴ࠻ࠢࡾࢁࠧኔ").format(bstack1ll1l111ll1_opy_))
        else:
            self.logger.info(bstack11l111_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥን").format(bstack1ll1l111ll1_opy_))
            with os.scandir(bstack1ll1l111ll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l1l1l11_opy_:
                        self.logger.info(bstack11l111_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥኖ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l111_opy_ (u"ࠨࠢኗ")
                        log_entry = bstack1ll11ll1l1l_opy_(
                            kind=bstack11l111_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤኘ"),
                            message=bstack11l111_opy_ (u"ࠣࠤኙ"),
                            level=bstack11l111_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨኚ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1llll11l1_opy_=entry.stat().st_size,
                            bstack1ll1111lll1_opy_=bstack11l111_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥኛ"),
                            bstack11ll1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll1l1ll1l1_opy_=hook.get(TestFramework.bstack1ll11l11l1l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l1l1l11_opy_.add(abs_path)
        hook[bstack11l111_opy_ (u"ࠦࡱࡵࡧࡴࠤኜ")] = logs
    def bstack1l1llll11ll_opy_(
        self,
        bstack1ll111llll1_opy_: bstack1lll1l1ll1l_opy_,
        entries: List[bstack1ll11ll1l1l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤኝ"))
        req.platform_index = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1llllllll11_opy_)
        req.execution_context.hash = str(bstack1ll111llll1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111llll1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111llll1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll11ll111_opy_)
            log_entry.uuid = entry.bstack1ll1111llll_opy_ if entry.bstack1ll1111llll_opy_ else TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll1lll1l1_opy_)
            log_entry.test_framework_state = bstack1ll111llll1_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧኞ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11l111_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤኟ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llll11l1_opy_
                log_entry.file_path = entry.bstack11ll1ll_opy_
        def bstack1ll11l1l1l1_opy_():
            bstack1l1ll1ll1_opy_ = datetime.now()
            try:
                self.bstack1llllll1l11_opy_.LogCreatedEvent(req)
                bstack1ll111llll1_opy_.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧአ"), datetime.now() - bstack1l1ll1ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࢁࡽࠣኡ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11l1l1l1_opy_)
    def __1ll1111l1l1_opy_(self, instance) -> None:
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡍࡱࡤࡨࡸࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡪࡧࡴࡦࡵࠣࡥࠥࡪࡩࡤࡶࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡩࡶࡴࡳࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡦࡴࡤࠡࡷࡳࡨࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡵࡷࡥࡹ࡫ࠠࡶࡵ࡬ࡲ࡬ࠦࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣኢ")
        bstack1ll11111ll1_opy_ = {bstack11l111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨኣ"): bstack1ll11111l1l_opy_.bstack1l1lll1llll_opy_()}
        TestFramework.bstack1ll11l11l11_opy_(instance, bstack1ll11111ll1_opy_)
    @staticmethod
    def __1l1llllll11_opy_(instance, args):
        request, bstack1ll1l1l1111_opy_ = args
        bstack1ll11l11lll_opy_ = id(bstack1ll1l1l1111_opy_)
        bstack1l1lllll111_opy_ = instance.data[TestFramework.bstack1ll11lll1ll_opy_]
        step = next(filter(lambda st: st[bstack11l111_opy_ (u"ࠬ࡯ࡤࠨኤ")] == bstack1ll11l11lll_opy_, bstack1l1lllll111_opy_[bstack11l111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬእ")]), None)
        step.update({
            bstack11l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫኦ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1l1lllll111_opy_[bstack11l111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኧ")]) if st[bstack11l111_opy_ (u"ࠩ࡬ࡨࠬከ")] == step[bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭ኩ")]), None)
        if index is not None:
            bstack1l1lllll111_opy_[bstack11l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኪ")][index] = step
        instance.data[TestFramework.bstack1ll11lll1ll_opy_] = bstack1l1lllll111_opy_
    @staticmethod
    def __1ll111l11ll_opy_(instance, args):
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡬ࡪࡴࠠ࡭ࡧࡱࠤࡦࡸࡧࡴࠢ࡬ࡷࠥ࠸ࠬࠡ࡫ࡷࠤࡸ࡯ࡧ࡯࡫ࡩ࡭ࡪࡹࠠࡵࡪࡨࡶࡪࠦࡩࡴࠢࡱࡳࠥ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡳࡩࡶࠤࡦࡸࡥࠡ࠯ࠣ࡟ࡷ࡫ࡱࡶࡧࡶࡸ࠱ࠦࡳࡵࡧࡳࡡࠏࠦࠠࠡࠢࠣࠤࠥࠦࡩࡧࠢࡤࡶ࡬ࡹࠠࡢࡴࡨࠤ࠸ࠦࡴࡩࡧࡱࠤࡹ࡮ࡥࠡ࡮ࡤࡷࡹࠦࡶࡢ࡮ࡸࡩࠥ࡯ࡳࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣካ")
        bstack1ll1l1ll11l_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1l1l1111_opy_ = args[1]
        bstack1ll11l11lll_opy_ = id(bstack1ll1l1l1111_opy_)
        bstack1l1lllll111_opy_ = instance.data[TestFramework.bstack1ll11lll1ll_opy_]
        step = None
        if bstack1ll11l11lll_opy_ is not None and bstack1l1lllll111_opy_.get(bstack11l111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኬ")):
            step = next(filter(lambda st: st[bstack11l111_opy_ (u"ࠧࡪࡦࠪክ")] == bstack1ll11l11lll_opy_, bstack1l1lllll111_opy_[bstack11l111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኮ")]), None)
            step.update({
                bstack11l111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧኯ"): bstack1ll1l1ll11l_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11l111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪኰ"): bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ኱"),
                bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ኲ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11l111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ኳ"): bstack11l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧኴ"),
                })
        index = next((i for i, st in enumerate(bstack1l1lllll111_opy_[bstack11l111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኵ")]) if st[bstack11l111_opy_ (u"ࠩ࡬ࡨࠬ኶")] == step[bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭኷")]), None)
        if index is not None:
            bstack1l1lllll111_opy_[bstack11l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኸ")][index] = step
        instance.data[TestFramework.bstack1ll11lll1ll_opy_] = bstack1l1lllll111_opy_
    @staticmethod
    def __1ll111ll1ll_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11l111_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧኹ")):
                examples = list(node.callspec.params[bstack11l111_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬኺ")].values())
            return examples
        except:
            return []
    def bstack1ll1l1l11ll_opy_(self, instance: bstack1lll1l1ll1l_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll11l111ll_opy_ = (
            PytestBDDFramework.bstack1ll111l1ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else PytestBDDFramework.bstack1ll111l111l_opy_
        )
        hook = PytestBDDFramework.bstack1ll11l1111l_opy_(instance, bstack1ll11l111ll_opy_)
        entries = hook.get(TestFramework.bstack1ll11l111l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_, []))
        return entries
    def bstack1ll1l11111l_opy_(self, instance: bstack1lll1l1ll1l_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll11l111ll_opy_ = (
            PytestBDDFramework.bstack1ll111l1ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else PytestBDDFramework.bstack1ll111l111l_opy_
        )
        PytestBDDFramework.bstack1ll1l1111ll_opy_(instance, bstack1ll11l111ll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_, []).clear()
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1lll1l1ll1l_opy_, bstack1ll11l111ll_opy_: str):
        bstack1ll11l1ll11_opy_ = (
            PytestBDDFramework.bstack1ll11ll1lll_opy_
            if bstack1ll11l111ll_opy_ == PytestBDDFramework.bstack1ll111l111l_opy_
            else PytestBDDFramework.bstack1l1lllllll1_opy_
        )
        bstack1ll1l111l1l_opy_ = TestFramework.get_state(instance, bstack1ll11l111ll_opy_, None)
        bstack1l1lllll1l1_opy_ = TestFramework.get_state(instance, bstack1ll11l1ll11_opy_, None) if bstack1ll1l111l1l_opy_ else None
        return (
            bstack1l1lllll1l1_opy_[bstack1ll1l111l1l_opy_][-1]
            if isinstance(bstack1l1lllll1l1_opy_, dict) and len(bstack1l1lllll1l1_opy_.get(bstack1ll1l111l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l1111ll_opy_(instance: bstack1lll1l1ll1l_opy_, bstack1ll11l111ll_opy_: str):
        hook = PytestBDDFramework.bstack1ll11l1111l_opy_(instance, bstack1ll11l111ll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l111l1_opy_, []).clear()
    @staticmethod
    def __1ll1111111l_opy_(instance: bstack1lll1l1ll1l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l111_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡣࡰࡴࡧࡷࠧኻ"), None)):
            return
        if os.getenv(bstack11l111_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡍࡑࡊࡗࠧኼ"), bstack11l111_opy_ (u"ࠤ࠴ࠦኽ")) != bstack11l111_opy_ (u"ࠥ࠵ࠧኾ"):
            PytestBDDFramework.logger.warning(bstack11l111_opy_ (u"ࠦ࡮࡭࡮ࡰࡴ࡬ࡲ࡬ࠦࡣࡢࡲ࡯ࡳ࡬ࠨ኿"))
            return
        bstack1l1llll1lll_opy_ = {
            bstack11l111_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦዀ"): (PytestBDDFramework.bstack1ll111l1ll1_opy_, PytestBDDFramework.bstack1l1lllllll1_opy_),
            bstack11l111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣ዁"): (PytestBDDFramework.bstack1ll111l111l_opy_, PytestBDDFramework.bstack1ll11ll1lll_opy_),
        }
        for when in (bstack11l111_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨዂ"), bstack11l111_opy_ (u"ࠣࡥࡤࡰࡱࠨዃ"), bstack11l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦዄ")):
            bstack1ll111l1lll_opy_ = args[1].get_records(when)
            if not bstack1ll111l1lll_opy_:
                continue
            records = [
                bstack1ll11ll1l1l_opy_(
                    kind=TestFramework.bstack1ll1111ll11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l111_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࡰࡤࡱࡪࠨዅ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l111_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࠧ዆")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll111l1lll_opy_
                if isinstance(getattr(r, bstack11l111_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨ዇"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11ll1l11_opy_, bstack1ll11l1ll11_opy_ = bstack1l1llll1lll_opy_.get(when, (None, None))
            bstack1ll11111l11_opy_ = TestFramework.get_state(instance, bstack1ll11ll1l11_opy_, None) if bstack1ll11ll1l11_opy_ else None
            bstack1l1lllll1l1_opy_ = TestFramework.get_state(instance, bstack1ll11l1ll11_opy_, None) if bstack1ll11111l11_opy_ else None
            if isinstance(bstack1l1lllll1l1_opy_, dict) and len(bstack1l1lllll1l1_opy_.get(bstack1ll11111l11_opy_, [])) > 0:
                hook = bstack1l1lllll1l1_opy_[bstack1ll11111l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l111l1_opy_ in hook:
                    hook[TestFramework.bstack1ll11l111l1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll111ll11l_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1l11l1l1_opy_(request.node, scenario)
        bstack1ll111l1l11_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll111l1l11_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1lll1l1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11l11l_opy_: test_id,
            TestFramework.bstack1ll1l11l111_opy_: test_name,
            TestFramework.bstack1l1llll1l11_opy_: test_id,
            TestFramework.bstack1l1llllllll_opy_: bstack1ll111l1l11_opy_,
            TestFramework.bstack1ll111l11l1_opy_: PytestBDDFramework.__1ll11l1l11l_opy_(feature, scenario),
            TestFramework.bstack1ll11lll111_opy_: code,
            TestFramework.bstack1llll1111l1_opy_: TestFramework.bstack1ll1l11lll1_opy_,
            TestFramework.bstack1lll11l111l_opy_: test_name
        }
    @staticmethod
    def __1ll1l11l1l1_opy_(node, scenario):
        if hasattr(node, bstack11l111_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨወ")):
            parts = node.nodeid.rsplit(bstack11l111_opy_ (u"ࠢ࡜ࠤዉ"))
            params = parts[-1]
            return bstack11l111_opy_ (u"ࠣࡽࢀࠤࡠࢁࡽࠣዊ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11l1l11l_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11l111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧዋ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11l111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨዌ")) else [])
    @staticmethod
    def __1ll11ll1111_opy_(location):
        return bstack11l111_opy_ (u"ࠦ࠿ࡀࠢው").join(filter(lambda x: isinstance(x, str), location))