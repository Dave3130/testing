# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11l1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack11ll1l111l_opy_ import bstack1ll1l1ll111_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1ll11_opy_,
    bstack1llll1111l1_opy_,
    bstack1lll1ll111l_opy_,
    bstack1ll11ll1111_opy_,
    bstack1ll11l111l1_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll11ll1l1l_opy_
from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll1l11l1ll_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
bstack1ll1l1l1111_opy_ = bstack1ll11ll1l1l_opy_()
bstack1ll1l1111ll_opy_ = bstack11ll_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥም")
bstack1ll11lll1ll_opy_ = bstack11ll_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢሞ")
bstack1l1lllllll1_opy_ = bstack11ll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦሟ")
bstack1l1lll1lll1_opy_ = 1.0
_1ll1111ll1l_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1l1llll1l1l_opy_ = bstack11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨሠ")
    bstack1ll111llll1_opy_ = bstack11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧሡ")
    bstack1ll111l1l1l_opy_ = bstack11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢሢ")
    bstack1ll11ll1lll_opy_ = bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦሣ")
    bstack1ll1l11l1l1_opy_ = bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨሤ")
    bstack1ll11111111_opy_: bool
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_  = None
    bstack1l1llll11ll_opy_ = [
        bstack1lll1l1ll11_opy_.BEFORE_ALL,
        bstack1lll1l1ll11_opy_.AFTER_ALL,
        bstack1lll1l1ll11_opy_.BEFORE_EACH,
        bstack1lll1l1ll11_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l1lllll1ll_opy_: Dict[str, str],
        bstack1ll111ll111_opy_: List[str]=[bstack11ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣሥ")],
        bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_ = None,
        bstack1lllll11111_opy_=None
    ):
        super().__init__(bstack1ll111ll111_opy_, bstack1l1lllll1ll_opy_, bstack1lll11l1l1l_opy_)
        self.bstack1ll11111111_opy_ = any(bstack11ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤሦ") in item.lower() for item in bstack1ll111ll111_opy_)
        self.bstack1lllll11111_opy_ = bstack1lllll11111_opy_
    def track_event(
        self,
        context: bstack1ll11ll1111_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1ll11_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1l1llll11ll_opy_:
            bstack1ll1l1ll111_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1ll11_opy_.NONE:
            self.logger.warning(bstack11ll_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢሧ") + str(test_hook_state) + bstack11ll_opy_ (u"ࠢࠣረ"))
            return
        if not self.bstack1ll11111111_opy_:
            self.logger.warning(bstack11ll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤሩ") + str(str(self.bstack1ll111ll111_opy_)) + bstack11ll_opy_ (u"ࠤࠥሪ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11ll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧራ") + str(kwargs) + bstack11ll_opy_ (u"ࠦࠧሬ"))
            return
        instance = self.__1ll1l1111l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11ll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦር") + str(args) + bstack11ll_opy_ (u"ࠨࠢሮ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1llll11ll_opy_ and test_hook_state == bstack1lll1ll111l_opy_.PRE:
                bstack1ll111l11ll_opy_ = bstack1llll11ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1l1lll11ll_opy_.value)
                name = str(EVENTS.bstack1l1lll11ll_opy_.name)+bstack11ll_opy_ (u"ࠢ࠻ࠤሯ")+str(test_framework_state.name)
                TestFramework.bstack1l1llll11l1_opy_(instance, name, bstack1ll111l11ll_opy_)
        except Exception as e:
            self.logger.debug(bstack11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧሰ").format(e))
        try:
            if test_framework_state == bstack1lll1l1ll11_opy_.TEST:
                if not TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1ll11111ll1_opy_) and test_hook_state == bstack1lll1ll111l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11l11l1l_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11ll_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሱ") + str(test_hook_state) + bstack11ll_opy_ (u"ࠥࠦሲ"))
                if test_hook_state == bstack1lll1ll111l_opy_.PRE and not TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1ll1l11l111_opy_):
                    TestFramework.bstack1llllll1lll_opy_(instance, TestFramework.bstack1ll1l11l111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1l1l1l1l_opy_(instance, args)
                    self.logger.debug(bstack11ll_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሳ") + str(test_hook_state) + bstack11ll_opy_ (u"ࠧࠨሴ"))
                elif test_hook_state == bstack1lll1ll111l_opy_.POST and not TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1l1lllll11l_opy_):
                    TestFramework.bstack1llllll1lll_opy_(instance, TestFramework.bstack1l1lllll11l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11ll_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤስ") + str(test_hook_state) + bstack11ll_opy_ (u"ࠢࠣሶ"))
            elif test_framework_state == bstack1lll1l1ll11_opy_.STEP:
                if test_hook_state == bstack1lll1ll111l_opy_.PRE:
                    PytestBDDFramework.__1l1llllll1l_opy_(instance, args)
                elif test_hook_state == bstack1lll1ll111l_opy_.POST:
                    PytestBDDFramework.__1l1lllll1l1_opy_(instance, args)
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG and test_hook_state == bstack1lll1ll111l_opy_.POST:
                PytestBDDFramework.__1ll111lll11_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG_REPORT and test_hook_state == bstack1lll1ll111l_opy_.POST:
                self.__1ll11111l11_opy_(instance, *args)
                self.__1ll111ll1ll_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1l1llll11ll_opy_:
                self.__1ll1l111l11_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11ll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤሷ") + str(instance.ref()) + bstack11ll_opy_ (u"ࠤࠥሸ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l1ll11l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1llll11ll_opy_ and test_hook_state == bstack1lll1ll111l_opy_.POST:
                name = str(EVENTS.bstack1l1lll11ll_opy_.name)+bstack11ll_opy_ (u"ࠥ࠾ࠧሹ")+str(test_framework_state.name)
                bstack1ll111l11ll_opy_ = TestFramework.bstack1ll11l1111l_opy_(instance, name)
                bstack1llll11ll11_opy_.end(EVENTS.bstack1l1lll11ll_opy_.value, bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦሺ"), bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥሻ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨሼ").format(e))
    def bstack1ll1l1l111l_opy_(self):
        return self.bstack1ll11111111_opy_
    def __1ll1l11llll_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11ll_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦሽ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l11lll1_opy_(rep, [bstack11ll_opy_ (u"ࠣࡹ࡫ࡩࡳࠨሾ"), bstack11ll_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥሿ"), bstack11ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥቀ"), bstack11ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦቁ"), bstack11ll_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨቂ"), bstack11ll_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧቃ")])
        return None
    def __1ll11111l11_opy_(self, instance: bstack1llll1111l1_opy_, *args):
        result = self.__1ll1l11llll_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111ll1_opy_ = None
        if result.get(bstack11ll_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣቄ"), None) == bstack11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣቅ") and len(args) > 1 and getattr(args[1], bstack11ll_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥቆ"), None) is not None:
            failure = [{bstack11ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ቇ"): [args[1].excinfo.exconly(), result.get(bstack11ll_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥቈ"), None)]}]
            bstack1111111ll1_opy_ = bstack11ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨ቉") if bstack11ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤቊ") in getattr(args[1].excinfo, bstack11ll_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤቋ"), bstack11ll_opy_ (u"ࠣࠤቌ")) else bstack11ll_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥቍ")
        bstack1ll11111lll_opy_ = result.get(bstack11ll_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦ቎"), TestFramework.bstack1ll1l111111_opy_)
        if bstack1ll11111lll_opy_ != TestFramework.bstack1ll1l111111_opy_:
            TestFramework.bstack1llllll1lll_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11lllll1_opy_(instance, {
            TestFramework.bstack1lll1l1111l_opy_: failure,
            TestFramework.bstack1l1llll1111_opy_: bstack1111111ll1_opy_,
            TestFramework.bstack1lll11ll11l_opy_: bstack1ll11111lll_opy_,
        })
    def __1ll1l1111l1_opy_(
        self,
        context: bstack1ll11ll1111_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1ll11_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l11ll11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1111l1ll_opy_ bstack1ll11llllll_opy_ this to be bstack11ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦ቏")
            if test_framework_state == bstack1lll1l1ll11_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11ll11l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11ll_opy_ (u"ࠧࡴ࡯ࡥࡧࠥቐ"), None), bstack11ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨቑ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11ll_opy_ (u"ࠢ࡯ࡱࡧࡩࠧቒ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣቓ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11l1lll1_opy_(target) if target else None
        return instance
    def __1ll1l111l11_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll111111l1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111llll1_opy_, {})
        if not key in bstack1ll111111l1_opy_:
            bstack1ll111111l1_opy_[key] = []
        bstack1l1llll111l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111l1l1l_opy_, {})
        if not key in bstack1l1llll111l_opy_:
            bstack1l1llll111l_opy_[key] = []
        bstack1ll11l111ll_opy_ = {
            PytestBDDFramework.bstack1ll111llll1_opy_: bstack1ll111111l1_opy_,
            PytestBDDFramework.bstack1ll111l1l1l_opy_: bstack1l1llll111l_opy_,
        }
        if test_hook_state == bstack1lll1ll111l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11ll_opy_ (u"ࠤ࡮ࡩࡾࠨቔ"): key,
                TestFramework.bstack1ll1l11ll1l_opy_: uuid4().__str__(),
                TestFramework.bstack1l1lllll111_opy_: TestFramework.bstack1ll111l1lll_opy_,
                TestFramework.bstack1ll11l1l111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1lll1ll11_opy_: [],
                TestFramework.bstack1ll1l11l11l_opy_: hook_name,
                TestFramework.bstack1ll1111l111_opy_: bstack1ll1l1l1ll1_opy_.bstack1ll1l1l1lll_opy_()
            }
            bstack1ll111111l1_opy_[key].append(hook)
            bstack1ll11l111ll_opy_[PytestBDDFramework.bstack1ll11ll1lll_opy_] = key
        elif test_hook_state == bstack1lll1ll111l_opy_.POST:
            bstack1l1lll1llll_opy_ = bstack1ll111111l1_opy_.get(key, [])
            hook = bstack1l1lll1llll_opy_.pop() if bstack1l1lll1llll_opy_ else None
            if hook:
                result = self.__1ll1l11llll_opy_(*args)
                if result:
                    bstack1ll11lll111_opy_ = result.get(bstack11ll_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦቕ"), TestFramework.bstack1ll111l1lll_opy_)
                    if bstack1ll11lll111_opy_ != TestFramework.bstack1ll111l1lll_opy_:
                        hook[TestFramework.bstack1l1lllll111_opy_] = bstack1ll11lll111_opy_
                hook[TestFramework.bstack1ll11l11111_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1111l111_opy_] = bstack1ll1l1l1ll1_opy_.bstack1ll1l1l1lll_opy_()
                self.bstack1ll11ll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll111l1l11_opy_, [])
                self.bstack1ll11l1l1l1_opy_(instance, logs)
                bstack1l1llll111l_opy_[key].append(hook)
                bstack1ll11l111ll_opy_[PytestBDDFramework.bstack1ll1l11l1l1_opy_] = key
        TestFramework.bstack1ll11lllll1_opy_(instance, bstack1ll11l111ll_opy_)
        self.logger.debug(bstack11ll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥቖ") + str(bstack1l1llll111l_opy_) + bstack11ll_opy_ (u"ࠧࠨ቗"))
    def __1ll1l11ll11_opy_(
        self,
        context: bstack1ll11ll1111_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l11lll1_opy_(args[0], [bstack11ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቘ"), bstack11ll_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣ቙"), bstack11ll_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣቚ"), bstack11ll_opy_ (u"ࠤ࡬ࡨࡸࠨቛ"), bstack11ll_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧቜ"), bstack11ll_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦቝ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11ll_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ቞")) else fixturedef.get(bstack11ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧ቟"), None)
        fixturename = request.fixturename if hasattr(request, bstack11ll_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧበ")) else None
        node = request.node if hasattr(request, bstack11ll_opy_ (u"ࠣࡰࡲࡨࡪࠨቡ")) else None
        target = request.node.nodeid if hasattr(node, bstack11ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤቢ")) else None
        baseid = fixturedef.get(bstack11ll_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥባ"), None) or bstack11ll_opy_ (u"ࠦࠧቤ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11ll_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥብ")):
            target = PytestBDDFramework.__1ll11lll11l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11ll_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣቦ")) else None
            if target and not TestFramework.bstack1ll11l1lll1_opy_(target):
                self.__1ll11ll11l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11ll_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤቧ") + str(test_hook_state) + bstack11ll_opy_ (u"ࠣࠤቨ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢቩ") + str(target) + bstack11ll_opy_ (u"ࠥࠦቪ"))
            return None
        instance = TestFramework.bstack1ll11l1lll1_opy_(target)
        if not instance:
            self.logger.warning(bstack11ll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨቫ") + str(target) + bstack11ll_opy_ (u"ࠧࠨቬ"))
            return None
        bstack1l1llll1l11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1llll1l1l_opy_, {})
        if os.getenv(bstack11ll_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢቭ"), bstack11ll_opy_ (u"ࠢ࠲ࠤቮ")) == bstack11ll_opy_ (u"ࠣ࠳ࠥቯ"):
            bstack1ll11l11ll1_opy_ = bstack11ll_opy_ (u"ࠤ࠽ࠦተ").join((scope, fixturename))
            bstack1ll11l1l11l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l111l1l_opy_ = {
                bstack11ll_opy_ (u"ࠥ࡯ࡪࡿࠢቱ"): bstack1ll11l11ll1_opy_,
                bstack11ll_opy_ (u"ࠦࡹࡧࡧࡴࠤቲ"): PytestBDDFramework.__1ll11l11lll_opy_(request.node, scenario),
                bstack11ll_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨታ"): fixturedef,
                bstack11ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቴ"): scope,
                bstack11ll_opy_ (u"ࠢࡵࡻࡳࡩࠧት"): None,
            }
            try:
                if test_hook_state == bstack1lll1ll111l_opy_.POST and callable(getattr(args[-1], bstack11ll_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧቶ"), None)):
                    bstack1ll1l111l1l_opy_[bstack11ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢቷ")] = TestFramework.bstack1ll111l111l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1ll111l_opy_.PRE:
                bstack1ll1l111l1l_opy_[bstack11ll_opy_ (u"ࠥࡹࡺ࡯ࡤࠣቸ")] = uuid4().__str__()
                bstack1ll1l111l1l_opy_[PytestBDDFramework.bstack1ll11l1l111_opy_] = bstack1ll11l1l11l_opy_
            elif test_hook_state == bstack1lll1ll111l_opy_.POST:
                bstack1ll1l111l1l_opy_[PytestBDDFramework.bstack1ll11l11111_opy_] = bstack1ll11l1l11l_opy_
            if bstack1ll11l11ll1_opy_ in bstack1l1llll1l11_opy_:
                bstack1l1llll1l11_opy_[bstack1ll11l11ll1_opy_].update(bstack1ll1l111l1l_opy_)
                self.logger.debug(bstack11ll_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧቹ") + str(bstack1l1llll1l11_opy_[bstack1ll11l11ll1_opy_]) + bstack11ll_opy_ (u"ࠧࠨቺ"))
            else:
                bstack1l1llll1l11_opy_[bstack1ll11l11ll1_opy_] = bstack1ll1l111l1l_opy_
                self.logger.debug(bstack11ll_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤቻ") + str(len(bstack1l1llll1l11_opy_)) + bstack11ll_opy_ (u"ࠢࠣቼ"))
        TestFramework.bstack1llllll1lll_opy_(instance, PytestBDDFramework.bstack1l1llll1l1l_opy_, bstack1l1llll1l11_opy_)
        self.logger.debug(bstack11ll_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣች") + str(instance.ref()) + bstack11ll_opy_ (u"ࠤࠥቾ"))
        return instance
    def __1ll11ll11l1_opy_(
        self,
        context: bstack1ll11ll1111_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        ob = bstack1llll1111l1_opy_(ctx, self.bstack1ll111ll111_opy_, self.bstack1l1lllll1ll_opy_, test_framework_state)
        TestFramework.bstack1ll11lllll1_opy_(ob, {
            TestFramework.bstack1lll1lllll1_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l11111_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l1l11l1_opy_: [],
            PytestBDDFramework.bstack1l1llll1l1l_opy_: {},
            PytestBDDFramework.bstack1ll111l1l1l_opy_: {},
            PytestBDDFramework.bstack1ll111llll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llllll1lll_opy_(ob, TestFramework.bstack1ll111l11l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llllll1lll_opy_(ob, TestFramework.bstack1llll1l111l_opy_, context.platform_index)
        TestFramework.bstack1lll1l11ll1_opy_[ctx.id] = ob
        self.logger.debug(bstack11ll_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥቿ") + str(TestFramework.bstack1lll1l11ll1_opy_.keys()) + bstack11ll_opy_ (u"ࠦࠧኀ"))
        return ob
    @staticmethod
    def __1ll1l1l1l1l_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll_opy_ (u"ࠬ࡯ࡤࠨኁ"): id(step),
                bstack11ll_opy_ (u"࠭ࡴࡦࡺࡷࠫኂ"): step.name,
                bstack11ll_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨኃ"): step.keyword,
            })
        meta = {
            bstack11ll_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩኄ"): {
                bstack11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧኅ"): feature.name,
                bstack11ll_opy_ (u"ࠪࡴࡦࡺࡨࠨኆ"): feature.filename,
                bstack11ll_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩኇ"): feature.description
            },
            bstack11ll_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧኈ"): {
                bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ኉"): scenario.name
            },
            bstack11ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኊ"): steps,
            bstack11ll_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪኋ"): PytestBDDFramework.__1ll1l111ll1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l1llllll11_opy_: meta
            }
        )
    def bstack1ll11ll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡴ࡫ࡰ࡭ࡱࡧࡲࠡࡶࡲࠤࡹ࡮ࡥࠡࡌࡤࡺࡦࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡃࡩࡧࡦ࡯ࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡬ࡲࡸ࡯ࡤࡦࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠳࡚ࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡵࡩࡵࡲࡡࡤࡧࡶࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦࠥ࡯࡮ࠡ࡫ࡷࡷࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡌࡪࠥࡧࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡯ࡤࡸࡨ࡮ࡥࡴࠢࡤࠤࡲࡵࡤࡪࡨ࡬ࡩࡩࠦࡨࡰࡱ࡮࠱ࡱ࡫ࡶࡦ࡮ࠣࡪ࡮ࡲࡥ࠭ࠢ࡬ࡸࠥࡩࡲࡦࡣࡷࡩࡸࠦࡡࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࠣࡻ࡮ࡺࡨࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡙ࠥࡩ࡮࡫࡯ࡥࡷࡲࡹ࠭ࠢ࡬ࡸࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡴࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡥࡽࠥࡸࡥࡱ࡮ࡤࡧ࡮ࡴࡧࠡࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡖ࡫ࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡤࡶࡪࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥ࡮࡯ࡰ࡭ࠪࡷࠥࠨ࡬ࡰࡩࡶࠦࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࠺ࠡࡖ࡫ࡩࠥ࡫ࡶࡦࡰࡷࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷࠥࡧ࡮ࡥࠢ࡫ࡳࡴࡱࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡘࡪࡹࡴࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣኌ")
        global _1ll1111ll1l_opy_
        platform_index = os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪኍ")]
        bstack1ll11llll1l_opy_ = os.path.join(bstack1ll1l1l1111_opy_, (bstack1ll1l1111ll_opy_ + str(platform_index)), bstack1ll11lll1ll_opy_)
        if not os.path.exists(bstack1ll11llll1l_opy_) or not os.path.isdir(bstack1ll11llll1l_opy_):
            return
        logs = hook.get(bstack11ll_opy_ (u"ࠦࡱࡵࡧࡴࠤ኎"), [])
        with os.scandir(bstack1ll11llll1l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1111ll1l_opy_:
                    self.logger.info(bstack11ll_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥ኏").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11ll_opy_ (u"ࠨࠢነ")
                    log_entry = bstack1ll11l111l1_opy_(
                        kind=bstack11ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤኑ"),
                        message=bstack11ll_opy_ (u"ࠣࠤኒ"),
                        level=bstack11ll_opy_ (u"ࠤࠥና"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll111111ll_opy_=entry.stat().st_size,
                        bstack1ll11ll1l11_opy_=bstack11ll_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥኔ"),
                        bstack1lllll_opy_=os.path.abspath(entry.path),
                        bstack1l1llll1lll_opy_=hook.get(TestFramework.bstack1ll1l11ll1l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1111ll1l_opy_.add(abs_path)
        platform_index = os.environ[bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫን")]
        bstack1ll1l11111l_opy_ = os.path.join(bstack1ll1l1l1111_opy_, (bstack1ll1l1111ll_opy_ + str(platform_index)), bstack1ll11lll1ll_opy_, bstack1l1lllllll1_opy_)
        if not os.path.exists(bstack1ll1l11111l_opy_) or not os.path.isdir(bstack1ll1l11111l_opy_):
            self.logger.info(bstack11ll_opy_ (u"ࠧࡔ࡯ࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡨࡲࡹࡳࡪࠠࡢࡶ࠽ࠤࢀࢃࠢኖ").format(bstack1ll1l11111l_opy_))
        else:
            self.logger.info(bstack11ll_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡧࡴࡲࡱࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠻ࠢࡾࢁࠧኗ").format(bstack1ll1l11111l_opy_))
            with os.scandir(bstack1ll1l11111l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1111ll1l_opy_:
                        self.logger.info(bstack11ll_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧኘ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11ll_opy_ (u"ࠣࠤኙ")
                        log_entry = bstack1ll11l111l1_opy_(
                            kind=bstack11ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦኚ"),
                            message=bstack11ll_opy_ (u"ࠥࠦኛ"),
                            level=bstack11ll_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣኜ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll111111ll_opy_=entry.stat().st_size,
                            bstack1ll11ll1l11_opy_=bstack11ll_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧኝ"),
                            bstack1lllll_opy_=os.path.abspath(entry.path),
                            bstack1ll111lll1l_opy_=hook.get(TestFramework.bstack1ll1l11ll1l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1111ll1l_opy_.add(abs_path)
        hook[bstack11ll_opy_ (u"ࠨ࡬ࡰࡩࡶࠦኞ")] = logs
    def bstack1ll11l1l1l1_opy_(
        self,
        bstack1ll11l1llll_opy_: bstack1llll1111l1_opy_,
        entries: List[bstack1ll11l111l1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦኟ"))
        req.platform_index = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1llll1l111l_opy_)
        req.execution_context.hash = str(bstack1ll11l1llll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l1llll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l1llll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1lll1lllll1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1lll1l11111_opy_)
            log_entry.uuid = entry.bstack1l1llll1lll_opy_ if entry.bstack1l1llll1lll_opy_ else TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1llll111l11_opy_)
            log_entry.test_framework_state = bstack1ll11l1llll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢአ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦኡ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111111ll_opy_
                log_entry.file_path = entry.bstack1lllll_opy_
        def bstack1ll11lll1l1_opy_():
            bstack1l11111lll_opy_ = datetime.now()
            try:
                self.bstack1lllll11111_opy_.LogCreatedEvent(req)
                bstack1ll11l1llll_opy_.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢኢ"), datetime.now() - bstack1l11111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡼࡿࠥኣ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11lll1l1_opy_)
    def __1ll111ll1ll_opy_(self, instance) -> None:
        bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡏࡳࡦࡪࡳࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡸࡥࡢࡶࡨࡷࠥࡧࠠࡥ࡫ࡦࡸࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡡ࡯ࡦࠣࡹࡵࡪࡡࡵࡧࡶࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡷࡹࡧࡴࡦࠢࡸࡷ࡮ࡴࡧࠡࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኤ")
        bstack1ll11l111ll_opy_ = {bstack11ll_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣእ"): bstack1ll1l1l1ll1_opy_.bstack1ll1l1l1lll_opy_()}
        TestFramework.bstack1ll11lllll1_opy_(instance, bstack1ll11l111ll_opy_)
    @staticmethod
    def __1l1llllll1l_opy_(instance, args):
        request, bstack1ll1l111lll_opy_ = args
        bstack1ll1111ll11_opy_ = id(bstack1ll1l111lll_opy_)
        bstack1ll1111l11l_opy_ = instance.data[TestFramework.bstack1l1llllll11_opy_]
        step = next(filter(lambda st: st[bstack11ll_opy_ (u"ࠧࡪࡦࠪኦ")] == bstack1ll1111ll11_opy_, bstack1ll1111l11l_opy_[bstack11ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኧ")]), None)
        step.update({
            bstack11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ከ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll1111l11l_opy_[bstack11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኩ")]) if st[bstack11ll_opy_ (u"ࠫ࡮ࡪࠧኪ")] == step[bstack11ll_opy_ (u"ࠬ࡯ࡤࠨካ")]), None)
        if index is not None:
            bstack1ll1111l11l_opy_[bstack11ll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኬ")][index] = step
        instance.data[TestFramework.bstack1l1llllll11_opy_] = bstack1ll1111l11l_opy_
    @staticmethod
    def __1l1lllll1l1_opy_(instance, args):
        bstack11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡮ࡥ࡯ࠢ࡯ࡩࡳࠦࡡࡳࡩࡶࠤ࡮ࡹࠠ࠳࠮ࠣ࡭ࡹࠦࡳࡪࡩࡱ࡭࡫࡯ࡥࡴࠢࡷ࡬ࡪࡸࡥࠡ࡫ࡶࠤࡳࡵࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࡸࠦࡡࡳࡧࠣ࠱ࠥࡡࡲࡦࡳࡸࡩࡸࡺࠬࠡࡵࡷࡩࡵࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠳ࠡࡶ࡫ࡩࡳࠦࡴࡩࡧࠣࡰࡦࡹࡴࠡࡸࡤࡰࡺ࡫ࠠࡪࡵࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥክ")
        bstack1ll1l1l11ll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1l111lll_opy_ = args[1]
        bstack1ll1111ll11_opy_ = id(bstack1ll1l111lll_opy_)
        bstack1ll1111l11l_opy_ = instance.data[TestFramework.bstack1l1llllll11_opy_]
        step = None
        if bstack1ll1111ll11_opy_ is not None and bstack1ll1111l11l_opy_.get(bstack11ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኮ")):
            step = next(filter(lambda st: st[bstack11ll_opy_ (u"ࠩ࡬ࡨࠬኯ")] == bstack1ll1111ll11_opy_, bstack1ll1111l11l_opy_[bstack11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኰ")]), None)
            step.update({
                bstack11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ኱"): bstack1ll1l1l11ll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬኲ"): bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ኳ"),
                bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨኴ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨኵ"): bstack11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ኶"),
                })
        index = next((i for i, st in enumerate(bstack1ll1111l11l_opy_[bstack11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ኷")]) if st[bstack11ll_opy_ (u"ࠫ࡮ࡪࠧኸ")] == step[bstack11ll_opy_ (u"ࠬ࡯ࡤࠨኹ")]), None)
        if index is not None:
            bstack1ll1111l11l_opy_[bstack11ll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኺ")][index] = step
        instance.data[TestFramework.bstack1l1llllll11_opy_] = bstack1ll1111l11l_opy_
    @staticmethod
    def __1ll1l111ll1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11ll_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩኻ")):
                examples = list(node.callspec.params[bstack11ll_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧኼ")].values())
            return examples
        except:
            return []
    def bstack1ll11ll11ll_opy_(self, instance: bstack1llll1111l1_opy_, bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_]):
        bstack1ll111l1ll1_opy_ = (
            PytestBDDFramework.bstack1ll11ll1lll_opy_
            if bstack1lllll1l11l_opy_[1] == bstack1lll1ll111l_opy_.PRE
            else PytestBDDFramework.bstack1ll1l11l1l1_opy_
        )
        hook = PytestBDDFramework.bstack1l1llllllll_opy_(instance, bstack1ll111l1ll1_opy_)
        entries = hook.get(TestFramework.bstack1l1lll1ll11_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l1l11l1_opy_, []))
        return entries
    def bstack1ll11llll11_opy_(self, instance: bstack1llll1111l1_opy_, bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_]):
        bstack1ll111l1ll1_opy_ = (
            PytestBDDFramework.bstack1ll11ll1lll_opy_
            if bstack1lllll1l11l_opy_[1] == bstack1lll1ll111l_opy_.PRE
            else PytestBDDFramework.bstack1ll1l11l1l1_opy_
        )
        PytestBDDFramework.bstack1ll111l1111_opy_(instance, bstack1ll111l1ll1_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l1l11l1_opy_, []).clear()
    @staticmethod
    def bstack1l1llllllll_opy_(instance: bstack1llll1111l1_opy_, bstack1ll111l1ll1_opy_: str):
        bstack1l1lll1ll1l_opy_ = (
            PytestBDDFramework.bstack1ll111l1l1l_opy_
            if bstack1ll111l1ll1_opy_ == PytestBDDFramework.bstack1ll1l11l1l1_opy_
            else PytestBDDFramework.bstack1ll111llll1_opy_
        )
        bstack1ll111lllll_opy_ = TestFramework.get_state(instance, bstack1ll111l1ll1_opy_, None)
        bstack1l1lll1l1ll_opy_ = TestFramework.get_state(instance, bstack1l1lll1ll1l_opy_, None) if bstack1ll111lllll_opy_ else None
        return (
            bstack1l1lll1l1ll_opy_[bstack1ll111lllll_opy_][-1]
            if isinstance(bstack1l1lll1l1ll_opy_, dict) and len(bstack1l1lll1l1ll_opy_.get(bstack1ll111lllll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll111l1111_opy_(instance: bstack1llll1111l1_opy_, bstack1ll111l1ll1_opy_: str):
        hook = PytestBDDFramework.bstack1l1llllllll_opy_(instance, bstack1ll111l1ll1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1lll1ll11_opy_, []).clear()
    @staticmethod
    def __1ll111lll11_opy_(instance: bstack1llll1111l1_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11ll_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡥࡲࡶࡩࡹࠢኽ"), None)):
            return
        if os.getenv(bstack11ll_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡏࡓࡌ࡙ࠢኾ"), bstack11ll_opy_ (u"ࠦ࠶ࠨ኿")) != bstack11ll_opy_ (u"ࠧ࠷ࠢዀ"):
            PytestBDDFramework.logger.warning(bstack11ll_opy_ (u"ࠨࡩࡨࡰࡲࡶ࡮ࡴࡧࠡࡥࡤࡴࡱࡵࡧࠣ዁"))
            return
        bstack1l1llll1ll1_opy_ = {
            bstack11ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨዂ"): (PytestBDDFramework.bstack1ll11ll1lll_opy_, PytestBDDFramework.bstack1ll111llll1_opy_),
            bstack11ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥዃ"): (PytestBDDFramework.bstack1ll1l11l1l1_opy_, PytestBDDFramework.bstack1ll111l1l1l_opy_),
        }
        for when in (bstack11ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣዄ"), bstack11ll_opy_ (u"ࠥࡧࡦࡲ࡬ࠣዅ"), bstack11ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ዆")):
            bstack1ll1111l1l1_opy_ = args[1].get_records(when)
            if not bstack1ll1111l1l1_opy_:
                continue
            records = [
                bstack1ll11l111l1_opy_(
                    kind=TestFramework.bstack1ll1l1l1l11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11ll_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠣ዇")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11ll_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪࠢወ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1111l1l1_opy_
                if isinstance(getattr(r, bstack11ll_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣዉ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1111111l_opy_, bstack1l1lll1ll1l_opy_ = bstack1l1llll1ll1_opy_.get(when, (None, None))
            bstack1ll11l11l11_opy_ = TestFramework.get_state(instance, bstack1ll1111111l_opy_, None) if bstack1ll1111111l_opy_ else None
            bstack1l1lll1l1ll_opy_ = TestFramework.get_state(instance, bstack1l1lll1ll1l_opy_, None) if bstack1ll11l11l11_opy_ else None
            if isinstance(bstack1l1lll1l1ll_opy_, dict) and len(bstack1l1lll1l1ll_opy_.get(bstack1ll11l11l11_opy_, [])) > 0:
                hook = bstack1l1lll1l1ll_opy_[bstack1ll11l11l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l1lll1ll11_opy_ in hook:
                    hook[TestFramework.bstack1l1lll1ll11_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l1l11l1_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11l11l1l_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll111ll1l1_opy_(request.node, scenario)
        bstack1ll11l1l1ll_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll11l1l1ll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll111l11_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11111ll1_opy_: test_id,
            TestFramework.bstack1ll11ll1ll1_opy_: test_name,
            TestFramework.bstack1ll111ll11l_opy_: test_id,
            TestFramework.bstack1ll1111llll_opy_: bstack1ll11l1l1ll_opy_,
            TestFramework.bstack1ll11111l1l_opy_: PytestBDDFramework.__1ll11l11lll_opy_(feature, scenario),
            TestFramework.bstack1ll1111lll1_opy_: code,
            TestFramework.bstack1lll11ll11l_opy_: TestFramework.bstack1ll1l111111_opy_,
            TestFramework.bstack1lll11l111l_opy_: test_name
        }
    @staticmethod
    def __1ll111ll1l1_opy_(node, scenario):
        if hasattr(node, bstack11ll_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪዊ")):
            parts = node.nodeid.rsplit(bstack11ll_opy_ (u"ࠤ࡞ࠦዋ"))
            params = parts[-1]
            return bstack11ll_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥዌ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11l11lll_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11ll_opy_ (u"ࠫࡹࡧࡧࡴࠩው")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11ll_opy_ (u"ࠬࡺࡡࡨࡵࠪዎ")) else [])
    @staticmethod
    def __1ll11lll11l_opy_(location):
        return bstack11ll_opy_ (u"ࠨ࠺࠻ࠤዏ").join(filter(lambda x: isinstance(x, str), location))