# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll1111l1l_opy_ import bstack1ll1ll1llll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1111111l1_opy_ import bstack1ll11l11111_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1lllll1_opy_,
    bstack1lll1l1ll11_opy_,
    bstack1llll1111l1_opy_,
    bstack1ll1l1lll11_opy_,
    bstack1ll111l1ll1_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l11ll11_opy_
from bstack_utils.bstack1l1l1111ll_opy_ import bstack111111111l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll11111l1l_opy_ import bstack1ll1l11111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
bstack1ll1l1l1ll1_opy_ = bstack1ll1l11ll11_opy_()
bstack1ll11ll1111_opy_ = bstack11l1l11_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᇱ")
bstack1ll1l1ll11l_opy_ = bstack11l1l11_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧᇲ")
bstack1ll11l11l11_opy_ = bstack11l1l11_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤᇳ")
bstack1l1lllll1ll_opy_ = 1.0
_1ll11lll1ll_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l111lll_opy_ = bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᇴ")
    bstack1ll11ll1lll_opy_ = bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࠥᇵ")
    bstack1ll11ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᇶ")
    bstack1ll11l11lll_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࠤᇷ")
    bstack1ll1l1lll1l_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᇸ")
    bstack1ll1ll111l1_opy_: bool
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_  = None
    bstack1ll11111ll1_opy_ = [
        bstack1lll1lllll1_opy_.BEFORE_ALL,
        bstack1lll1lllll1_opy_.AFTER_ALL,
        bstack1lll1lllll1_opy_.BEFORE_EACH,
        bstack1lll1lllll1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll1l1ll1l1_opy_: Dict[str, str],
        bstack1ll11ll1l11_opy_: List[str]=[bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᇹ")],
        bstack1lll1l11111_opy_: bstack1lll11lllll_opy_ = None,
        bstack1llll1ll11l_opy_=None
    ):
        super().__init__(bstack1ll11ll1l11_opy_, bstack1ll1l1ll1l1_opy_, bstack1lll1l11111_opy_)
        self.bstack1ll1ll111l1_opy_ = any(bstack11l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᇺ") in item.lower() for item in bstack1ll11ll1l11_opy_)
        self.bstack1llll1ll11l_opy_ = bstack1llll1ll11l_opy_
    def track_event(
        self,
        context: bstack1ll1l1lll11_opy_,
        test_framework_state: bstack1lll1lllll1_opy_,
        test_hook_state: bstack1llll1111l1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1lllll1_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll11111ll1_opy_:
            bstack1ll11l11111_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1lllll1_opy_.NONE:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨࡨࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࠧᇻ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠧࠨᇼ"))
            return
        if not self.bstack1ll1ll111l1_opy_:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡃࠢᇽ") + str(str(self.bstack1ll11ll1l11_opy_)) + bstack11l1l11_opy_ (u"ࠢࠣᇾ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇿ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠤࠥሀ"))
            return
        instance = self.__1ll1l1111ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡥࡷ࡭ࡳ࠾ࠤሁ") + str(args) + bstack11l1l11_opy_ (u"ࠦࠧሂ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11111ll1_opy_ and test_hook_state == bstack1llll1111l1_opy_.PRE:
                bstack1ll11lll11l_opy_ = bstack111111111l_opy_.bstack1ll1111llll_opy_(EVENTS.bstack111ll1lll_opy_.value)
                name = str(EVENTS.bstack111ll1lll_opy_.name)+bstack11l1l11_opy_ (u"ࠧࡀࠢሃ")+str(test_framework_state.name)
                TestFramework.bstack1ll111111l1_opy_(instance, name, bstack1ll11lll11l_opy_)
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳࠢࡳࡶࡪࡀࠠࡼࡿࠥሄ").format(e))
        try:
            if test_framework_state == bstack1lll1lllll1_opy_.TEST:
                if not TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll1l11llll_opy_) and test_hook_state == bstack1llll1111l1_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11l111ll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡭ࡱࡤࡨࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢህ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠣࠤሆ"))
                if test_hook_state == bstack1llll1111l1_opy_.PRE and not TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll1111ll11_opy_):
                    TestFramework.bstack1llll1l1l1l_opy_(instance, TestFramework.bstack1ll1111ll11_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll111l1lll_opy_(instance, args)
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡸࡺࡡࡳࡶࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢሇ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠥࠦለ"))
                elif test_hook_state == bstack1llll1111l1_opy_.POST and not TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_):
                    TestFramework.bstack1llll1l1l1l_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡥ࡯ࡦࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢሉ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠧࠨሊ"))
            elif test_framework_state == bstack1lll1lllll1_opy_.STEP:
                if test_hook_state == bstack1llll1111l1_opy_.PRE:
                    PytestBDDFramework.__1ll1l111111_opy_(instance, args)
                elif test_hook_state == bstack1llll1111l1_opy_.POST:
                    PytestBDDFramework.__1l1lllllll1_opy_(instance, args)
            elif test_framework_state == bstack1lll1lllll1_opy_.LOG and test_hook_state == bstack1llll1111l1_opy_.POST:
                PytestBDDFramework.__1ll1111l1l1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1lllll1_opy_.LOG_REPORT and test_hook_state == bstack1llll1111l1_opy_.POST:
                self.__1l1lllll1l1_opy_(instance, *args)
                self.__1ll11lllll1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll11111ll1_opy_:
                self.__1ll1l11l1l1_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢላ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠢࠣሌ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l1111l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11111ll1_opy_ and test_hook_state == bstack1llll1111l1_opy_.POST:
                name = str(EVENTS.bstack111ll1lll_opy_.name)+bstack11l1l11_opy_ (u"ࠣ࠼ࠥል")+str(test_framework_state.name)
                bstack1ll11lll11l_opy_ = TestFramework.bstack1ll111l111l_opy_(instance, name)
                bstack111111111l_opy_.end(EVENTS.bstack111ll1lll_opy_.value, bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤሎ"), bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠥ࠾ࡪࡴࡤࠣሏ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦሐ").format(e))
    def bstack1ll1l1l11l1_opy_(self):
        return self.bstack1ll1ll111l1_opy_
    def __1ll1111111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤሑ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l11lll1_opy_(rep, [bstack11l1l11_opy_ (u"ࠨࡷࡩࡧࡱࠦሒ"), bstack11l1l11_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣሓ"), bstack11l1l11_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣሔ"), bstack11l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤሕ"), bstack11l1l11_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠦሖ"), bstack11l1l11_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥሗ")])
        return None
    def __1l1lllll1l1_opy_(self, instance: bstack1lll1l1ll11_opy_, *args):
        result = self.__1ll1111111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l111l_opy_ = None
        if result.get(bstack11l1l11_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨመ"), None) == bstack11l1l11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨሙ") and len(args) > 1 and getattr(args[1], bstack11l1l11_opy_ (u"ࠢࡦࡺࡦ࡭ࡳ࡬࡯ࠣሚ"), None) is not None:
            failure = [{bstack11l1l11_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫማ"): [args[1].excinfo.exconly(), result.get(bstack11l1l11_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣሜ"), None)]}]
            bstack11111l111l_opy_ = bstack11l1l11_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦም") if bstack11l1l11_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢሞ") in getattr(args[1].excinfo, bstack11l1l11_opy_ (u"ࠧࡺࡹࡱࡧࡱࡥࡲ࡫ࠢሟ"), bstack11l1l11_opy_ (u"ࠨࠢሠ")) else bstack11l1l11_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣሡ")
        bstack1ll1111l111_opy_ = result.get(bstack11l1l11_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤሢ"), TestFramework.bstack1ll11lll1l1_opy_)
        if bstack1ll1111l111_opy_ != TestFramework.bstack1ll11lll1l1_opy_:
            TestFramework.bstack1llll1l1l1l_opy_(instance, TestFramework.bstack1ll111lll1l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1l1lllll11l_opy_(instance, {
            TestFramework.bstack1lll1ll1ll1_opy_: failure,
            TestFramework.bstack1ll111ll1ll_opy_: bstack11111l111l_opy_,
            TestFramework.bstack1llll111ll1_opy_: bstack1ll1111l111_opy_,
        })
    def __1ll1l1111ll_opy_(
        self,
        context: bstack1ll1l1lll11_opy_,
        test_framework_state: bstack1lll1lllll1_opy_,
        test_hook_state: bstack1llll1111l1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1lllll1_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l1l1l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1llll1ll1_opy_ bstack1l1llll1lll_opy_ this to be bstack11l1l11_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሣ")
            if test_framework_state == bstack1lll1lllll1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l1ll1ll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1lllll1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l1l11_opy_ (u"ࠥࡲࡴࡪࡥࠣሤ"), None), bstack11l1l11_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሥ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧࠥሦ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11l1l11_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨሧ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11111111_opy_(target) if target else None
        return instance
    def __1ll1l11l1l1_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        test_framework_state: bstack1lll1lllll1_opy_,
        test_hook_state: bstack1llll1111l1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll11l1l11l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll1lll_opy_, {})
        if not key in bstack1ll11l1l11l_opy_:
            bstack1ll11l1l11l_opy_[key] = []
        bstack1ll1111lll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll11ll_opy_, {})
        if not key in bstack1ll1111lll1_opy_:
            bstack1ll1111lll1_opy_[key] = []
        bstack1ll11llll11_opy_ = {
            PytestBDDFramework.bstack1ll11ll1lll_opy_: bstack1ll11l1l11l_opy_,
            PytestBDDFramework.bstack1ll11ll11ll_opy_: bstack1ll1111lll1_opy_,
        }
        if test_hook_state == bstack1llll1111l1_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11l1l11_opy_ (u"ࠢ࡬ࡧࡼࠦረ"): key,
                TestFramework.bstack1ll111ll111_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l1ll111_opy_: TestFramework.bstack1ll11ll1l1l_opy_,
                TestFramework.bstack1ll1l1llll1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11ll11l1_opy_: [],
                TestFramework.bstack1ll111l11ll_opy_: hook_name,
                TestFramework.bstack1ll111lllll_opy_: bstack1ll1l11111l_opy_.bstack1ll1111ll1l_opy_()
            }
            bstack1ll11l1l11l_opy_[key].append(hook)
            bstack1ll11llll11_opy_[PytestBDDFramework.bstack1ll11l11lll_opy_] = key
        elif test_hook_state == bstack1llll1111l1_opy_.POST:
            bstack1l1llllllll_opy_ = bstack1ll11l1l11l_opy_.get(key, [])
            hook = bstack1l1llllllll_opy_.pop() if bstack1l1llllllll_opy_ else None
            if hook:
                result = self.__1ll1111111l_opy_(*args)
                if result:
                    bstack1ll1l111l11_opy_ = result.get(bstack11l1l11_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤሩ"), TestFramework.bstack1ll11ll1l1l_opy_)
                    if bstack1ll1l111l11_opy_ != TestFramework.bstack1ll11ll1l1l_opy_:
                        hook[TestFramework.bstack1ll1l1ll111_opy_] = bstack1ll1l111l11_opy_
                hook[TestFramework.bstack1ll11l1l1l1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll111lllll_opy_] = bstack1ll1l11111l_opy_.bstack1ll1111ll1l_opy_()
                self.bstack1ll111l1l11_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l1l1lll_opy_, [])
                self.bstack1l1llllll11_opy_(instance, logs)
                bstack1ll1111lll1_opy_[key].append(hook)
                bstack1ll11llll11_opy_[PytestBDDFramework.bstack1ll1l1lll1l_opy_] = key
        TestFramework.bstack1l1lllll11l_opy_(instance, bstack1ll11llll11_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡪࡲࡳࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽ࡮ࡩࡾࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࡁࢀ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࢂࠦࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࠽ࠣሪ") + str(bstack1ll1111lll1_opy_) + bstack11l1l11_opy_ (u"ࠥࠦራ"))
    def __1ll1l1l1l1l_opy_(
        self,
        context: bstack1ll1l1lll11_opy_,
        test_framework_state: bstack1lll1lllll1_opy_,
        test_hook_state: bstack1llll1111l1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l11lll1_opy_(args[0], [bstack11l1l11_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥሬ"), bstack11l1l11_opy_ (u"ࠧࡧࡲࡨࡰࡤࡱࡪࠨር"), bstack11l1l11_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨሮ"), bstack11l1l11_opy_ (u"ࠢࡪࡦࡶࠦሯ"), bstack11l1l11_opy_ (u"ࠣࡷࡱ࡭ࡹࡺࡥࡴࡶࠥሰ"), bstack11l1l11_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤሱ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11l1l11_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤሲ")) else fixturedef.get(bstack11l1l11_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥሳ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l1l11_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥሴ")) else None
        node = request.node if hasattr(request, bstack11l1l11_opy_ (u"ࠨ࡮ࡰࡦࡨࠦስ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l1l11_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢሶ")) else None
        baseid = fixturedef.get(bstack11l1l11_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣሷ"), None) or bstack11l1l11_opy_ (u"ࠤࠥሸ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l1l11_opy_ (u"ࠥࡣࡵࡿࡦࡶࡰࡦ࡭ࡹ࡫࡭ࠣሹ")):
            target = PytestBDDFramework.__1ll11ll111l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l1l11_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨሺ")) else None
            if target and not TestFramework.bstack1ll11111111_opy_(target):
                self.__1ll1l1ll1ll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠ࡯ࡱࡧࡩࡂࢁ࡮ࡰࡦࡨࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢሻ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠨࠢሼ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࡂࢁࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧሽ") + str(target) + bstack11l1l11_opy_ (u"ࠣࠤሾ"))
            return None
        instance = TestFramework.bstack1ll11111111_opy_(target)
        if not instance:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡤࡤࡷࡪ࡯ࡤ࠾ࡽࡥࡥࡸ࡫ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦሿ") + str(target) + bstack11l1l11_opy_ (u"ࠥࠦቀ"))
            return None
        bstack1ll11l1ll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l111lll_opy_, {})
        if os.getenv(bstack11l1l11_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡊࡎ࡞ࡔࡖࡔࡈࡗࠧቁ"), bstack11l1l11_opy_ (u"ࠧ࠷ࠢቂ")) == bstack11l1l11_opy_ (u"ࠨ࠱ࠣቃ"):
            bstack1ll11l1111l_opy_ = bstack11l1l11_opy_ (u"ࠢ࠻ࠤቄ").join((scope, fixturename))
            bstack1ll1l1l1l11_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l1l1111_opy_ = {
                bstack11l1l11_opy_ (u"ࠣ࡭ࡨࡽࠧቅ"): bstack1ll11l1111l_opy_,
                bstack11l1l11_opy_ (u"ࠤࡷࡥ࡬ࡹࠢቆ"): PytestBDDFramework.__1ll11llll1l_opy_(request.node, scenario),
                bstack11l1l11_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࠦቇ"): fixturedef,
                bstack11l1l11_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥቈ"): scope,
                bstack11l1l11_opy_ (u"ࠧࡺࡹࡱࡧࠥ቉"): None,
            }
            try:
                if test_hook_state == bstack1llll1111l1_opy_.POST and callable(getattr(args[-1], bstack11l1l11_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥቊ"), None)):
                    bstack1ll1l1l1111_opy_[bstack11l1l11_opy_ (u"ࠢࡵࡻࡳࡩࠧቋ")] = TestFramework.bstack1ll111l1l1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1llll1111l1_opy_.PRE:
                bstack1ll1l1l1111_opy_[bstack11l1l11_opy_ (u"ࠣࡷࡸ࡭ࡩࠨቌ")] = uuid4().__str__()
                bstack1ll1l1l1111_opy_[PytestBDDFramework.bstack1ll1l1llll1_opy_] = bstack1ll1l1l1l11_opy_
            elif test_hook_state == bstack1llll1111l1_opy_.POST:
                bstack1ll1l1l1111_opy_[PytestBDDFramework.bstack1ll11l1l1l1_opy_] = bstack1ll1l1l1l11_opy_
            if bstack1ll11l1111l_opy_ in bstack1ll11l1ll11_opy_:
                bstack1ll11l1ll11_opy_[bstack1ll11l1111l_opy_].update(bstack1ll1l1l1111_opy_)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࠥቍ") + str(bstack1ll11l1ll11_opy_[bstack1ll11l1111l_opy_]) + bstack11l1l11_opy_ (u"ࠥࠦ቎"))
            else:
                bstack1ll11l1ll11_opy_[bstack1ll11l1111l_opy_] = bstack1ll1l1l1111_opy_
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࡾࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡿࠣࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࠢ቏") + str(len(bstack1ll11l1ll11_opy_)) + bstack11l1l11_opy_ (u"ࠧࠨቐ"))
        TestFramework.bstack1llll1l1l1l_opy_(instance, PytestBDDFramework.bstack1ll1l111lll_opy_, bstack1ll11l1ll11_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࡼ࡮ࡨࡲ࠭ࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠪࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨቑ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠢࠣቒ"))
        return instance
    def __1ll1l1ll1ll_opy_(
        self,
        context: bstack1ll1l1lll11_opy_,
        test_framework_state: bstack1lll1lllll1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1llll_opy_.create_context(target)
        ob = bstack1lll1l1ll11_opy_(ctx, self.bstack1ll11ll1l11_opy_, self.bstack1ll1l1ll1l1_opy_, test_framework_state)
        TestFramework.bstack1l1lllll11l_opy_(ob, {
            TestFramework.bstack1lll1l11l1l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1111l_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l11l1ll_opy_: [],
            PytestBDDFramework.bstack1ll1l111lll_opy_: {},
            PytestBDDFramework.bstack1ll11ll11ll_opy_: {},
            PytestBDDFramework.bstack1ll11ll1lll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l1l1l_opy_(ob, TestFramework.bstack1ll1ll11111_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l1l1l_opy_(ob, TestFramework.bstack1llll1ll111_opy_, context.platform_index)
        TestFramework.bstack1lll1lll111_opy_[ctx.id] = ob
        self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡦࡸࡽ࠴ࡩࡥ࠿ࡾࡧࡹࡾ࠮ࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣቓ") + str(TestFramework.bstack1lll1lll111_opy_.keys()) + bstack11l1l11_opy_ (u"ࠤࠥቔ"))
        return ob
    @staticmethod
    def __1ll111l1lll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࠭ቕ"): id(step),
                bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡸࡵࠩቖ"): step.name,
                bstack11l1l11_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭቗"): step.keyword,
            })
        meta = {
            bstack11l1l11_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧቘ"): {
                bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ቙"): feature.name,
                bstack11l1l11_opy_ (u"ࠨࡲࡤࡸ࡭࠭ቚ"): feature.filename,
                bstack11l1l11_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧቛ"): feature.description
            },
            bstack11l1l11_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬቜ"): {
                bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩቝ"): scenario.name
            },
            bstack11l1l11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ቞"): steps,
            bstack11l1l11_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨ቟"): PytestBDDFramework.__1ll11ll1ll1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll111l11l1_opy_: meta
            }
        )
    def bstack1ll111l1l11_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡹࡩ࡮࡫࡯ࡥࡷࠦࡴࡰࠢࡷ࡬ࡪࠦࡊࡢࡸࡤࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪ࡬ࡷࠥࡳࡥࡵࡪࡲࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡈ࡮ࡥࡤ࡭ࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡇࡱࡵࠤࡪࡧࡣࡩࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸ࠲ࠠࡳࡧࡳࡰࡦࡩࡥࡴࠢࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤࠣ࡭ࡳࠦࡩࡵࡵࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡊࡨࠣࡥࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡩࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡭ࡢࡶࡦ࡬ࡪࡹࠠࡢࠢࡰࡳࡩ࡯ࡦࡪࡧࡧࠤ࡭ࡵ࡯࡬࠯࡯ࡩࡻ࡫࡬ࠡࡨ࡬ࡰࡪ࠲ࠠࡪࡶࠣࡧࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࠡࡹ࡬ࡸ࡭ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡗ࡮ࡳࡩ࡭ࡣࡵࡰࡾ࠲ࠠࡪࡶࠣࡴࡷࡵࡣࡦࡵࡶࡩࡸࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡ࡮ࡲࡧࡦࡺࡥࡥࠢ࡬ࡲࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡣࡻࠣࡶࡪࡶ࡬ࡢࡥ࡬ࡲ࡬ࠦࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡔࡩࡧࠣࡧࡷ࡫ࡡࡵࡧࡧࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡢࡴࡨࠤࡦࡪࡤࡦࡦࠣࡸࡴࠦࡴࡩࡧࠣ࡬ࡴࡵ࡫ࠨࡵࠣࠦࡱࡵࡧࡴࠤࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯࠿ࠦࡔࡩࡧࠣࡩࡻ࡫࡮ࡵࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵࠣࡥࡳࡪࠠࡩࡱࡲ࡯ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨበ")
        global _1ll11lll1ll_opy_
        platform_index = os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨቡ")]
        bstack1ll1l11l111_opy_ = os.path.join(bstack1ll1l1l1ll1_opy_, (bstack1ll11ll1111_opy_ + str(platform_index)), bstack1ll1l1ll11l_opy_)
        if not os.path.exists(bstack1ll1l11l111_opy_) or not os.path.isdir(bstack1ll1l11l111_opy_):
            return
        logs = hook.get(bstack11l1l11_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢቢ"), [])
        with os.scandir(bstack1ll1l11l111_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11lll1ll_opy_:
                    self.logger.info(bstack11l1l11_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣባ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l1l11_opy_ (u"ࠦࠧቤ")
                    log_entry = bstack1ll111l1ll1_opy_(
                        kind=bstack11l1l11_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢብ"),
                        message=bstack11l1l11_opy_ (u"ࠨࠢቦ"),
                        level=bstack11l1l11_opy_ (u"ࠢࠣቧ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll111ll11l_opy_=entry.stat().st_size,
                        bstack1ll1l11ll1l_opy_=bstack11l1l11_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣቨ"),
                        bstack111l11l_opy_=os.path.abspath(entry.path),
                        bstack1ll1ll111ll_opy_=hook.get(TestFramework.bstack1ll111ll111_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11lll1ll_opy_.add(abs_path)
        platform_index = os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩቩ")]
        bstack1ll111111ll_opy_ = os.path.join(bstack1ll1l1l1ll1_opy_, (bstack1ll11ll1111_opy_ + str(platform_index)), bstack1ll1l1ll11l_opy_, bstack1ll11l11l11_opy_)
        if not os.path.exists(bstack1ll111111ll_opy_) or not os.path.isdir(bstack1ll111111ll_opy_):
            self.logger.info(bstack11l1l11_opy_ (u"ࠥࡒࡴࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡦࡰࡷࡱࡨࠥࡧࡴ࠻ࠢࡾࢁࠧቪ").format(bstack1ll111111ll_opy_))
        else:
            self.logger.info(bstack11l1l11_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥቫ").format(bstack1ll111111ll_opy_))
            with os.scandir(bstack1ll111111ll_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11lll1ll_opy_:
                        self.logger.info(bstack11l1l11_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥቬ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l1l11_opy_ (u"ࠨࠢቭ")
                        log_entry = bstack1ll111l1ll1_opy_(
                            kind=bstack11l1l11_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤቮ"),
                            message=bstack11l1l11_opy_ (u"ࠣࠤቯ"),
                            level=bstack11l1l11_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨተ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll111ll11l_opy_=entry.stat().st_size,
                            bstack1ll1l11ll1l_opy_=bstack11l1l11_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥቱ"),
                            bstack111l11l_opy_=os.path.abspath(entry.path),
                            bstack1ll11l1l111_opy_=hook.get(TestFramework.bstack1ll111ll111_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11lll1ll_opy_.add(abs_path)
        hook[bstack11l1l11_opy_ (u"ࠦࡱࡵࡧࡴࠤቲ")] = logs
    def bstack1l1llllll11_opy_(
        self,
        bstack1l1llllll1l_opy_: bstack1lll1l1ll11_opy_,
        entries: List[bstack1ll111l1ll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤታ"))
        req.platform_index = TestFramework.get_state(bstack1l1llllll1l_opy_, TestFramework.bstack1llll1ll111_opy_)
        req.execution_context.hash = str(bstack1l1llllll1l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1llllll1l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1llllll1l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1llllll1l_opy_, TestFramework.bstack1lll1l11l1l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1llllll1l_opy_, TestFramework.bstack1lll1l1111l_opy_)
            log_entry.uuid = entry.bstack1ll1ll111ll_opy_ if entry.bstack1ll1ll111ll_opy_ else TestFramework.get_state(bstack1l1llllll1l_opy_, TestFramework.bstack1llll11l1ll_opy_)
            log_entry.test_framework_state = bstack1l1llllll1l_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l1l11_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧቴ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11l1l11_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤት"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111ll11l_opy_
                log_entry.file_path = entry.bstack111l11l_opy_
        def bstack1ll11l11ll1_opy_():
            bstack1l11lll1l_opy_ = datetime.now()
            try:
                self.bstack1llll1ll11l_opy_.LogCreatedEvent(req)
                bstack1l1llllll1l_opy_.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧቶ"), datetime.now() - bstack1l11lll1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1l11_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࢁࡽࠣቷ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll11l11ll1_opy_)
    def __1ll11lllll1_opy_(self, instance) -> None:
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡍࡱࡤࡨࡸࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡪࡧࡴࡦࡵࠣࡥࠥࡪࡩࡤࡶࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡩࡶࡴࡳࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡦࡴࡤࠡࡷࡳࡨࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡵࡷࡥࡹ࡫ࠠࡶࡵ࡬ࡲ࡬ࠦࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣቸ")
        bstack1ll11llll11_opy_ = {bstack11l1l11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨቹ"): bstack1ll1l11111l_opy_.bstack1ll1111ll1l_opy_()}
        TestFramework.bstack1l1lllll11l_opy_(instance, bstack1ll11llll11_opy_)
    @staticmethod
    def __1ll1l111111_opy_(instance, args):
        request, bstack1ll1l111l1l_opy_ = args
        bstack1ll11lll111_opy_ = id(bstack1ll1l111l1l_opy_)
        bstack1ll11l1l1ll_opy_ = instance.data[TestFramework.bstack1ll111l11l1_opy_]
        step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠬ࡯ࡤࠨቺ")] == bstack1ll11lll111_opy_, bstack1ll11l1l1ll_opy_[bstack11l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬቻ")]), None)
        step.update({
            bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫቼ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11l1l1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧች")]) if st[bstack11l1l11_opy_ (u"ࠩ࡬ࡨࠬቾ")] == step[bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࠭ቿ")]), None)
        if index is not None:
            bstack1ll11l1l1ll_opy_[bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኀ")][index] = step
        instance.data[TestFramework.bstack1ll111l11l1_opy_] = bstack1ll11l1l1ll_opy_
    @staticmethod
    def __1l1lllllll1_opy_(instance, args):
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡬ࡪࡴࠠ࡭ࡧࡱࠤࡦࡸࡧࡴࠢ࡬ࡷࠥ࠸ࠬࠡ࡫ࡷࠤࡸ࡯ࡧ࡯࡫ࡩ࡭ࡪࡹࠠࡵࡪࡨࡶࡪࠦࡩࡴࠢࡱࡳࠥ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡳࡩࡶࠤࡦࡸࡥࠡ࠯ࠣ࡟ࡷ࡫ࡱࡶࡧࡶࡸ࠱ࠦࡳࡵࡧࡳࡡࠏࠦࠠࠡࠢࠣࠤࠥࠦࡩࡧࠢࡤࡶ࡬ࡹࠠࡢࡴࡨࠤ࠸ࠦࡴࡩࡧࡱࠤࡹ࡮ࡥࠡ࡮ࡤࡷࡹࠦࡶࡢ࡮ࡸࡩࠥ࡯ࡳࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣኁ")
        bstack1ll1l1lllll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1l111l1l_opy_ = args[1]
        bstack1ll11lll111_opy_ = id(bstack1ll1l111l1l_opy_)
        bstack1ll11l1l1ll_opy_ = instance.data[TestFramework.bstack1ll111l11l1_opy_]
        step = None
        if bstack1ll11lll111_opy_ is not None and bstack1ll11l1l1ll_opy_.get(bstack11l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኂ")):
            step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠧࡪࡦࠪኃ")] == bstack1ll11lll111_opy_, bstack1ll11l1l1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኄ")]), None)
            step.update({
                bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧኅ"): bstack1ll1l1lllll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11l1l11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪኆ"): bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫኇ"),
                bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ኈ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11l1l11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭኉"): bstack11l1l11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧኊ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11l1l1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኋ")]) if st[bstack11l1l11_opy_ (u"ࠩ࡬ࡨࠬኌ")] == step[bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࠭ኍ")]), None)
        if index is not None:
            bstack1ll11l1l1ll_opy_[bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ኎")][index] = step
        instance.data[TestFramework.bstack1ll111l11l1_opy_] = bstack1ll11l1l1ll_opy_
    @staticmethod
    def __1ll11ll1ll1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11l1l11_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧ኏")):
                examples = list(node.callspec.params[bstack11l1l11_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬነ")].values())
            return examples
        except:
            return []
    def bstack1ll111lll11_opy_(self, instance: bstack1lll1l1ll11_opy_, bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_]):
        bstack1ll11l11l1l_opy_ = (
            PytestBDDFramework.bstack1ll11l11lll_opy_
            if bstack11111111l1_opy_[1] == bstack1llll1111l1_opy_.PRE
            else PytestBDDFramework.bstack1ll1l1lll1l_opy_
        )
        hook = PytestBDDFramework.bstack1ll11111l11_opy_(instance, bstack1ll11l11l1l_opy_)
        entries = hook.get(TestFramework.bstack1ll11ll11l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l11l1ll_opy_, []))
        return entries
    def bstack1ll11l1llll_opy_(self, instance: bstack1lll1l1ll11_opy_, bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_]):
        bstack1ll11l11l1l_opy_ = (
            PytestBDDFramework.bstack1ll11l11lll_opy_
            if bstack11111111l1_opy_[1] == bstack1llll1111l1_opy_.PRE
            else PytestBDDFramework.bstack1ll1l1lll1l_opy_
        )
        PytestBDDFramework.bstack1ll1l111ll1_opy_(instance, bstack1ll11l11l1l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l11l1ll_opy_, []).clear()
    @staticmethod
    def bstack1ll11111l11_opy_(instance: bstack1lll1l1ll11_opy_, bstack1ll11l11l1l_opy_: str):
        bstack1ll1l1l11ll_opy_ = (
            PytestBDDFramework.bstack1ll11ll11ll_opy_
            if bstack1ll11l11l1l_opy_ == PytestBDDFramework.bstack1ll1l1lll1l_opy_
            else PytestBDDFramework.bstack1ll11ll1lll_opy_
        )
        bstack1ll1111l1ll_opy_ = TestFramework.get_state(instance, bstack1ll11l11l1l_opy_, None)
        bstack1ll11l111l1_opy_ = TestFramework.get_state(instance, bstack1ll1l1l11ll_opy_, None) if bstack1ll1111l1ll_opy_ else None
        return (
            bstack1ll11l111l1_opy_[bstack1ll1111l1ll_opy_][-1]
            if isinstance(bstack1ll11l111l1_opy_, dict) and len(bstack1ll11l111l1_opy_.get(bstack1ll1111l1ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l111ll1_opy_(instance: bstack1lll1l1ll11_opy_, bstack1ll11l11l1l_opy_: str):
        hook = PytestBDDFramework.bstack1ll11111l11_opy_(instance, bstack1ll11l11l1l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11ll11l1_opy_, []).clear()
    @staticmethod
    def __1ll1111l1l1_opy_(instance: bstack1lll1l1ll11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l1l11_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡣࡰࡴࡧࡷࠧኑ"), None)):
            return
        if os.getenv(bstack11l1l11_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡍࡑࡊࡗࠧኒ"), bstack11l1l11_opy_ (u"ࠤ࠴ࠦና")) != bstack11l1l11_opy_ (u"ࠥ࠵ࠧኔ"):
            PytestBDDFramework.logger.warning(bstack11l1l11_opy_ (u"ࠦ࡮࡭࡮ࡰࡴ࡬ࡲ࡬ࠦࡣࡢࡲ࡯ࡳ࡬ࠨን"))
            return
        bstack1ll111l1111_opy_ = {
            bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦኖ"): (PytestBDDFramework.bstack1ll11l11lll_opy_, PytestBDDFramework.bstack1ll11ll1lll_opy_),
            bstack11l1l11_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣኗ"): (PytestBDDFramework.bstack1ll1l1lll1l_opy_, PytestBDDFramework.bstack1ll11ll11ll_opy_),
        }
        for when in (bstack11l1l11_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨኘ"), bstack11l1l11_opy_ (u"ࠣࡥࡤࡰࡱࠨኙ"), bstack11l1l11_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦኚ")):
            bstack1ll1ll11l11_opy_ = args[1].get_records(when)
            if not bstack1ll1ll11l11_opy_:
                continue
            records = [
                bstack1ll111l1ll1_opy_(
                    kind=TestFramework.bstack1ll1111l11l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l1l11_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࡰࡤࡱࡪࠨኛ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l1l11_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࠧኜ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1ll11l11_opy_
                if isinstance(getattr(r, bstack11l1l11_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨኝ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111ll1l1_opy_, bstack1ll1l1l11ll_opy_ = bstack1ll111l1111_opy_.get(when, (None, None))
            bstack1ll11l1ll1l_opy_ = TestFramework.get_state(instance, bstack1ll111ll1l1_opy_, None) if bstack1ll111ll1l1_opy_ else None
            bstack1ll11l111l1_opy_ = TestFramework.get_state(instance, bstack1ll1l1l11ll_opy_, None) if bstack1ll11l1ll1l_opy_ else None
            if isinstance(bstack1ll11l111l1_opy_, dict) and len(bstack1ll11l111l1_opy_.get(bstack1ll11l1ll1l_opy_, [])) > 0:
                hook = bstack1ll11l111l1_opy_[bstack1ll11l1ll1l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11ll11l1_opy_ in hook:
                    hook[TestFramework.bstack1ll11ll11l1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l11l1ll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11l111ll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1ll1111l_opy_(request.node, scenario)
        bstack1l1lllll111_opy_ = feature.filename
        if not test_id or not test_name or not bstack1l1lllll111_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll11l1ll_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11llll_opy_: test_id,
            TestFramework.bstack1ll11111lll_opy_: test_name,
            TestFramework.bstack1ll11llllll_opy_: test_id,
            TestFramework.bstack1ll11l1lll1_opy_: bstack1l1lllll111_opy_,
            TestFramework.bstack1ll1l1l111l_opy_: PytestBDDFramework.__1ll11llll1l_opy_(feature, scenario),
            TestFramework.bstack1ll111llll1_opy_: code,
            TestFramework.bstack1llll111ll1_opy_: TestFramework.bstack1ll11lll1l1_opy_,
            TestFramework.bstack1lll11l1l1l_opy_: test_name
        }
    @staticmethod
    def __1ll1ll1111l_opy_(node, scenario):
        if hasattr(node, bstack11l1l11_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨኞ")):
            parts = node.nodeid.rsplit(bstack11l1l11_opy_ (u"ࠢ࡜ࠤኟ"))
            params = parts[-1]
            return bstack11l1l11_opy_ (u"ࠣࡽࢀࠤࡠࢁࡽࠣአ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11llll1l_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11l1l11_opy_ (u"ࠩࡷࡥ࡬ࡹࠧኡ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11l1l11_opy_ (u"ࠪࡸࡦ࡭ࡳࠨኢ")) else [])
    @staticmethod
    def __1ll11ll111l_opy_(location):
        return bstack11l1l11_opy_ (u"ࠦ࠿ࡀࠢኣ").join(filter(lambda x: isinstance(x, str), location))