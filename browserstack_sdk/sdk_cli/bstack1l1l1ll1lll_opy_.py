# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1lll11l1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l111ll_opy_ import bstack1ll1l11ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll11l1ll_opy_,
    bstack1lll1l11l11_opy_,
    bstack1llll1l11l1_opy_,
    bstack1ll1l1ll111_opy_,
    bstack1ll1l1l1ll1_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1111l1ll_opy_
from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11llll11_opy_ import bstack1ll11l11ll1_opy_
from bstack_utils.bstack1ll1ll1l_opy_ import bstack1llll111_opy_
bstack1ll11l1111l_opy_ = bstack1ll1111l1ll_opy_()
bstack1ll11l11lll_opy_ = 1.0
bstack1ll11ll11ll_opy_ = bstack1lllll1_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᕪ")
bstack11llll1ll1l_opy_ = bstack1lllll1_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᕫ")
bstack11llll1lll1_opy_ = bstack1lllll1_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᕬ")
bstack11llll1ll11_opy_ = bstack1lllll1_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢᕭ")
bstack11llll1l1ll_opy_ = bstack1lllll1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦᕮ")
_1ll11l11l11_opy_ = set()
class bstack1l1l1l111l1_opy_(TestFramework):
    bstack1ll11ll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᕯ")
    bstack1ll1ll11l1l_opy_ = bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧᕰ")
    bstack1ll1ll11111_opy_ = bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᕱ")
    bstack1ll111l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦᕲ")
    bstack1ll1ll1111l_opy_ = bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᕳ")
    bstack1ll11111lll_opy_: bool
    bstack1lll11lllll_opy_: bstack1lll1l1111l_opy_  = None
    bstack1111111l1l_opy_ = None
    bstack1ll111l1l1l_opy_ = [
        bstack1llll11l1ll_opy_.BEFORE_ALL,
        bstack1llll11l1ll_opy_.AFTER_ALL,
        bstack1llll11l1ll_opy_.BEFORE_EACH,
        bstack1llll11l1ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l1llllllll_opy_: Dict[str, str],
        bstack1ll11l1l1l1_opy_: List[str]=[bstack1lllll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᕴ")],
        bstack1lll11lllll_opy_: bstack1lll1l1111l_opy_=None,
        bstack1111111l1l_opy_=None
    ):
        super().__init__(bstack1ll11l1l1l1_opy_, bstack1l1llllllll_opy_, bstack1lll11lllll_opy_)
        self.bstack1ll11111lll_opy_ = any(bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᕵ") in item.lower() for item in bstack1ll11l1l1l1_opy_)
        self.bstack1111111l1l_opy_ = bstack1111111l1l_opy_
    def track_event(
        self,
        context: bstack1ll1l1ll111_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll11l1ll_opy_.TEST or test_framework_state in bstack1l1l1l111l1_opy_.bstack1ll111l1l1l_opy_:
            bstack1ll1l11ll1l_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll11l1ll_opy_.NONE:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢᕶ") + str(test_hook_state) + bstack1lllll1_opy_ (u"ࠢࠣᕷ"))
            return
        if not self.bstack1ll11111lll_opy_:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤᕸ") + str(str(self.bstack1ll11l1l1l1_opy_)) + bstack1lllll1_opy_ (u"ࠤࠥᕹ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᕺ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠦࠧᕻ"))
            return
        instance = self.__1ll11lll1l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦᕼ") + str(args) + bstack1lllll1_opy_ (u"ࠨࠢᕽ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l1l111l1_opy_.bstack1ll111l1l1l_opy_ and test_hook_state == bstack1llll1l11l1_opy_.PRE:
                bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack11l1lllll1_opy_.value)
                name = str(EVENTS.bstack11l1lllll1_opy_.name)+bstack1lllll1_opy_ (u"ࠢ࠻ࠤᕾ")+str(test_framework_state.name)
                TestFramework.bstack1ll11l1lll1_opy_(instance, name, bstack1ll1l1l1111_opy_)
        except Exception as e:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧᕿ").format(e))
        try:
            if not TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll1l1l1lll_opy_) and test_hook_state == bstack1llll1l11l1_opy_.PRE:
                test = bstack1l1l1l111l1_opy_.__1ll1l1llll1_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖀ") + str(test_hook_state) + bstack1lllll1_opy_ (u"ࠥࠦᖁ"))
            if test_framework_state == bstack1llll11l1ll_opy_.TEST:
                if test_hook_state == bstack1llll1l11l1_opy_.PRE and not TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll1ll11l11_opy_):
                    TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1ll1ll11l11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖂ") + str(test_hook_state) + bstack1lllll1_opy_ (u"ࠧࠨᖃ"))
                elif test_hook_state == bstack1llll1l11l1_opy_.POST and not TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll1111l11l_opy_):
                    TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1ll1111l11l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖄ") + str(test_hook_state) + bstack1lllll1_opy_ (u"ࠢࠣᖅ"))
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG and test_hook_state == bstack1llll1l11l1_opy_.POST:
                bstack1l1l1l111l1_opy_.__1ll11llllll_opy_(instance, *args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG_REPORT and test_hook_state == bstack1llll1l11l1_opy_.POST:
                self.__1ll1ll111ll_opy_(instance, *args)
                self.__1l1lllll111_opy_(instance)
            elif test_framework_state in bstack1l1l1l111l1_opy_.bstack1ll111l1l1l_opy_:
                self.__1ll1111l1l1_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᖆ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠤࠥᖇ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11lll1ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l1l111l1_opy_.bstack1ll111l1l1l_opy_ and test_hook_state == bstack1llll1l11l1_opy_.POST:
                name = str(EVENTS.bstack11l1lllll1_opy_.name)+bstack1lllll1_opy_ (u"ࠥ࠾ࠧᖈ")+str(test_framework_state.name)
                bstack1ll1l1l1111_opy_ = TestFramework.bstack1ll111l1111_opy_(instance, name)
                bstack1lllllllll1_opy_.end(EVENTS.bstack11l1lllll1_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᖉ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᖊ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᖋ").format(e))
    def bstack1ll11ll1ll1_opy_(self):
        return self.bstack1ll11111lll_opy_
    def __1ll1l1111ll_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1lllll1_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᖌ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l11l111_opy_(rep, [bstack1lllll1_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᖍ"), bstack1lllll1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖎ"), bstack1lllll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᖏ"), bstack1lllll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᖐ"), bstack1lllll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨᖑ"), bstack1lllll1_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᖒ")])
        return None
    def __1ll1ll111ll_opy_(self, instance: bstack1lll1l11l11_opy_, *args):
        result = self.__1ll1l1111ll_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l11ll_opy_ = None
        if result.get(bstack1lllll1_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖓ"), None) == bstack1lllll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᖔ") and len(args) > 1 and getattr(args[1], bstack1lllll1_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥᖕ"), None) is not None:
            failure = [{bstack1lllll1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᖖ"): [args[1].excinfo.exconly(), result.get(bstack1lllll1_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥᖗ"), None)]}]
            bstack11111l11ll_opy_ = bstack1lllll1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᖘ") if bstack1lllll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᖙ") in getattr(args[1].excinfo, bstack1lllll1_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤᖚ"), bstack1lllll1_opy_ (u"ࠣࠤᖛ")) else bstack1lllll1_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᖜ")
        bstack1ll1l1l11ll_opy_ = result.get(bstack1lllll1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖝ"), TestFramework.bstack1ll111l11ll_opy_)
        if bstack1ll1l1l11ll_opy_ != TestFramework.bstack1ll111l11ll_opy_:
            TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1ll111lllll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11ll1111_opy_(instance, {
            TestFramework.bstack1lll1l1llll_opy_: failure,
            TestFramework.bstack1ll11llll1l_opy_: bstack11111l11ll_opy_,
            TestFramework.bstack1lll1ll1111_opy_: bstack1ll1l1l11ll_opy_,
        })
    def __1ll11lll1l1_opy_(
        self,
        context: bstack1ll1l1ll111_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll11l1ll_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l1lll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l11lll1_opy_ bstack1ll11l111l1_opy_ this to be bstack1lllll1_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᖞ")
            if test_framework_state == bstack1llll11l1ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1111111l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1lllll1_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᖟ"), None), bstack1lllll1_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖠ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1lllll1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᖡ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11lll11l_opy_(target) if target else None
        return instance
    def __1ll1111l1l1_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll11ll111l_opy_ = TestFramework.get_state(instance, bstack1l1l1l111l1_opy_.bstack1ll1ll11l1l_opy_, {})
        if not key in bstack1ll11ll111l_opy_:
            bstack1ll11ll111l_opy_[key] = []
        bstack1ll1l1l111l_opy_ = TestFramework.get_state(instance, bstack1l1l1l111l1_opy_.bstack1ll1ll11111_opy_, {})
        if not key in bstack1ll1l1l111l_opy_:
            bstack1ll1l1l111l_opy_[key] = []
        bstack1ll111lll11_opy_ = {
            bstack1l1l1l111l1_opy_.bstack1ll1ll11l1l_opy_: bstack1ll11ll111l_opy_,
            bstack1l1l1l111l1_opy_.bstack1ll1ll11111_opy_: bstack1ll1l1l111l_opy_,
        }
        if test_hook_state == bstack1llll1l11l1_opy_.PRE:
            hook = {
                bstack1lllll1_opy_ (u"ࠣ࡭ࡨࡽࠧᖢ"): key,
                TestFramework.bstack1ll11l11111_opy_: uuid4().__str__(),
                TestFramework.bstack1ll111l1lll_opy_: TestFramework.bstack1l1llll1lll_opy_,
                TestFramework.bstack1ll1l1ll1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll111ll1l1_opy_: [],
                TestFramework.bstack1ll1l111lll_opy_: args[1] if len(args) > 1 else bstack1lllll1_opy_ (u"ࠩࠪᖣ"),
                TestFramework.bstack1ll1111llll_opy_: bstack1ll11l11ll1_opy_.bstack1ll111ll1ll_opy_()
            }
            bstack1ll11ll111l_opy_[key].append(hook)
            bstack1ll111lll11_opy_[bstack1l1l1l111l1_opy_.bstack1ll111l1ll1_opy_] = key
        elif test_hook_state == bstack1llll1l11l1_opy_.POST:
            bstack1ll111l111l_opy_ = bstack1ll11ll111l_opy_.get(key, [])
            hook = bstack1ll111l111l_opy_.pop() if bstack1ll111l111l_opy_ else None
            if hook:
                result = self.__1ll1l1111ll_opy_(*args)
                if result:
                    bstack1ll1l11llll_opy_ = result.get(bstack1lllll1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖤ"), TestFramework.bstack1l1llll1lll_opy_)
                    if bstack1ll1l11llll_opy_ != TestFramework.bstack1l1llll1lll_opy_:
                        hook[TestFramework.bstack1ll111l1lll_opy_] = bstack1ll1l11llll_opy_
                hook[TestFramework.bstack1ll111llll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1111llll_opy_]= bstack1ll11l11ll1_opy_.bstack1ll111ll1ll_opy_()
                self.bstack1ll1l11ll11_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l11l1l1_opy_, [])
                if logs: self.bstack1ll11111l11_opy_(instance, logs)
                bstack1ll1l1l111l_opy_[key].append(hook)
                bstack1ll111lll11_opy_[bstack1l1l1l111l1_opy_.bstack1ll1ll1111l_opy_] = key
        TestFramework.bstack1ll11ll1111_opy_(instance, bstack1ll111lll11_opy_)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥᖥ") + str(bstack1ll1l1l111l_opy_) + bstack1lllll1_opy_ (u"ࠧࠨᖦ"))
    def __1ll1l1lll1l_opy_(
        self,
        context: bstack1ll1l1ll111_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l11l111_opy_(args[0], [bstack1lllll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᖧ"), bstack1lllll1_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᖨ"), bstack1lllll1_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᖩ"), bstack1lllll1_opy_ (u"ࠤ࡬ࡨࡸࠨᖪ"), bstack1lllll1_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᖫ"), bstack1lllll1_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦᖬ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1lllll1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᖭ")) else fixturedef.get(bstack1lllll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᖮ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1lllll1_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧᖯ")) else None
        node = request.node if hasattr(request, bstack1lllll1_opy_ (u"ࠣࡰࡲࡨࡪࠨᖰ")) else None
        target = request.node.nodeid if hasattr(node, bstack1lllll1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᖱ")) else None
        baseid = fixturedef.get(bstack1lllll1_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᖲ"), None) or bstack1lllll1_opy_ (u"ࠦࠧᖳ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1lllll1_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥᖴ")):
            target = bstack1l1l1l111l1_opy_.__1ll1l1lll11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1lllll1_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᖵ")) else None
            if target and not TestFramework.bstack1ll11lll11l_opy_(target):
                self.__1ll1111111l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖶ") + str(test_hook_state) + bstack1lllll1_opy_ (u"ࠣࠤᖷ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢᖸ") + str(target) + bstack1lllll1_opy_ (u"ࠥࠦᖹ"))
            return None
        instance = TestFramework.bstack1ll11lll11l_opy_(target)
        if not instance:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᖺ") + str(target) + bstack1lllll1_opy_ (u"ࠧࠨᖻ"))
            return None
        bstack1ll111ll11l_opy_ = TestFramework.get_state(instance, bstack1l1l1l111l1_opy_.bstack1ll11ll1l1l_opy_, {})
        if os.getenv(bstack1lllll1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢᖼ"), bstack1lllll1_opy_ (u"ࠢ࠲ࠤᖽ")) == bstack1lllll1_opy_ (u"ࠣ࠳ࠥᖾ"):
            bstack1ll1l1111l1_opy_ = bstack1lllll1_opy_ (u"ࠤ࠽ࠦᖿ").join((scope, fixturename))
            bstack1ll1l11111l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1ll111l1_opy_ = {
                bstack1lllll1_opy_ (u"ࠥ࡯ࡪࡿࠢᗀ"): bstack1ll1l1111l1_opy_,
                bstack1lllll1_opy_ (u"ࠦࡹࡧࡧࡴࠤᗁ"): bstack1l1l1l111l1_opy_.__1ll1111ll11_opy_(request.node),
                bstack1lllll1_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨᗂ"): fixturedef,
                bstack1lllll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗃ"): scope,
                bstack1lllll1_opy_ (u"ࠢࡵࡻࡳࡩࠧᗄ"): None,
            }
            try:
                if test_hook_state == bstack1llll1l11l1_opy_.POST and callable(getattr(args[-1], bstack1lllll1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᗅ"), None)):
                    bstack1ll1ll111l1_opy_[bstack1lllll1_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᗆ")] = TestFramework.bstack1ll1l1ll1ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1llll1l11l1_opy_.PRE:
                bstack1ll1ll111l1_opy_[bstack1lllll1_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᗇ")] = uuid4().__str__()
                bstack1ll1ll111l1_opy_[bstack1l1l1l111l1_opy_.bstack1ll1l1ll1l1_opy_] = bstack1ll1l11111l_opy_
            elif test_hook_state == bstack1llll1l11l1_opy_.POST:
                bstack1ll1ll111l1_opy_[bstack1l1l1l111l1_opy_.bstack1ll111llll1_opy_] = bstack1ll1l11111l_opy_
            if bstack1ll1l1111l1_opy_ in bstack1ll111ll11l_opy_:
                bstack1ll111ll11l_opy_[bstack1ll1l1111l1_opy_].update(bstack1ll1ll111l1_opy_)
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧᗈ") + str(bstack1ll111ll11l_opy_[bstack1ll1l1111l1_opy_]) + bstack1lllll1_opy_ (u"ࠧࠨᗉ"))
            else:
                bstack1ll111ll11l_opy_[bstack1ll1l1111l1_opy_] = bstack1ll1ll111l1_opy_
                self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤᗊ") + str(len(bstack1ll111ll11l_opy_)) + bstack1lllll1_opy_ (u"ࠢࠣᗋ"))
        TestFramework.bstack1lllll1l11l_opy_(instance, bstack1l1l1l111l1_opy_.bstack1ll11ll1l1l_opy_, bstack1ll111ll11l_opy_)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᗌ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠤࠥᗍ"))
        return instance
    def __1ll1111111l_opy_(
        self,
        context: bstack1ll1l1ll111_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll11l1_opy_.create_context(target)
        ob = bstack1lll1l11l11_opy_(ctx, self.bstack1ll11l1l1l1_opy_, self.bstack1l1llllllll_opy_, test_framework_state)
        TestFramework.bstack1ll11ll1111_opy_(ob, {
            TestFramework.bstack1lll1ll1l1l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1llllll_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1l1ll_opy_: [],
            bstack1l1l1l111l1_opy_.bstack1ll11ll1l1l_opy_: {},
            bstack1l1l1l111l1_opy_.bstack1ll1ll11111_opy_: {},
            bstack1l1l1l111l1_opy_.bstack1ll1ll11l1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll1l11l_opy_(ob, TestFramework.bstack1ll11l1ll11_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll1l11l_opy_(ob, TestFramework.bstack1111111ll1_opy_, context.platform_index)
        TestFramework.bstack1lll1llll11_opy_[ctx.id] = ob
        self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᗎ") + str(TestFramework.bstack1lll1llll11_opy_.keys()) + bstack1lllll1_opy_ (u"ࠦࠧᗏ"))
        return ob
    def bstack1ll1l111111_opy_(self, instance: bstack1lll1l11l11_opy_, bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_]):
        bstack1l1llllll1l_opy_ = (
            bstack1l1l1l111l1_opy_.bstack1ll111l1ll1_opy_
            if bstack1lllll111ll_opy_[1] == bstack1llll1l11l1_opy_.PRE
            else bstack1l1l1l111l1_opy_.bstack1ll1ll1111l_opy_
        )
        hook = bstack1l1l1l111l1_opy_.bstack1ll111l1l11_opy_(instance, bstack1l1llllll1l_opy_)
        entries = hook.get(TestFramework.bstack1ll111ll1l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, []))
        return entries
    def bstack1ll11lllll1_opy_(self, instance: bstack1lll1l11l11_opy_, bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_]):
        bstack1l1llllll1l_opy_ = (
            bstack1l1l1l111l1_opy_.bstack1ll111l1ll1_opy_
            if bstack1lllll111ll_opy_[1] == bstack1llll1l11l1_opy_.PRE
            else bstack1l1l1l111l1_opy_.bstack1ll1ll1111l_opy_
        )
        bstack1l1l1l111l1_opy_.bstack1ll111ll111_opy_(instance, bstack1l1llllll1l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, []).clear()
    def bstack1ll1l11ll11_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1lllll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᗐ")
        global _1ll11l11l11_opy_
        platform_index = os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᗑ")]
        bstack1ll11l1llll_opy_ = os.path.join(bstack1ll11l1111l_opy_, (bstack1ll11ll11ll_opy_ + str(platform_index)), bstack11llll1ll11_opy_)
        if not os.path.exists(bstack1ll11l1llll_opy_) or not os.path.isdir(bstack1ll11l1llll_opy_):
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷࡷࠥࡺ࡯ࠡࡲࡵࡳࡨ࡫ࡳࡴࠢࡾࢁࠧᗒ").format(bstack1ll11l1llll_opy_))
            return
        logs = hook.get(bstack1lllll1_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᗓ"), [])
        with os.scandir(bstack1ll11l1llll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l11l11_opy_:
                    self.logger.info(bstack1lllll1_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢᗔ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1lllll1_opy_ (u"ࠥࠦᗕ")
                    log_entry = bstack1ll1l1l1ll1_opy_(
                        kind=bstack1lllll1_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᗖ"),
                        message=bstack1lllll1_opy_ (u"ࠧࠨᗗ"),
                        level=bstack1lllll1_opy_ (u"ࠨࠢᗘ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll1l1ll11l_opy_=entry.stat().st_size,
                        bstack1ll1l11l1ll_opy_=bstack1lllll1_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᗙ"),
                        bstack11l1l11_opy_=os.path.abspath(entry.path),
                        bstack1ll11l1l11l_opy_=hook.get(TestFramework.bstack1ll11l11111_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l11l11_opy_.add(abs_path)
        platform_index = os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᗚ")]
        bstack1ll11lll111_opy_ = os.path.join(bstack1ll11l1111l_opy_, (bstack1ll11ll11ll_opy_ + str(platform_index)), bstack11llll1ll11_opy_, bstack11llll1l1ll_opy_)
        if not os.path.exists(bstack1ll11lll111_opy_) or not os.path.isdir(bstack1ll11lll111_opy_):
            self.logger.info(bstack1lllll1_opy_ (u"ࠤࡑࡳࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡬࡯ࡶࡰࡧࠤࡦࡺ࠺ࠡࡽࢀࠦᗛ").format(bstack1ll11lll111_opy_))
        else:
            self.logger.info(bstack1lllll1_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᗜ").format(bstack1ll11lll111_opy_))
            with os.scandir(bstack1ll11lll111_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l11l11_opy_:
                        self.logger.info(bstack1lllll1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᗝ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1lllll1_opy_ (u"ࠧࠨᗞ")
                        log_entry = bstack1ll1l1l1ll1_opy_(
                            kind=bstack1lllll1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᗟ"),
                            message=bstack1lllll1_opy_ (u"ࠢࠣᗠ"),
                            level=bstack1lllll1_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᗡ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll1l1ll11l_opy_=entry.stat().st_size,
                            bstack1ll1l11l1ll_opy_=bstack1lllll1_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᗢ"),
                            bstack11l1l11_opy_=os.path.abspath(entry.path),
                            bstack1ll1111l111_opy_=hook.get(TestFramework.bstack1ll11l11111_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l11l11_opy_.add(abs_path)
        hook[bstack1lllll1_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᗣ")] = logs
    def bstack1ll11111l11_opy_(
        self,
        bstack1l1lllll1ll_opy_: bstack1lll1l11l11_opy_,
        entries: List[bstack1ll1l1l1ll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1lllll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣᗤ"))
        req.platform_index = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1111111ll1_opy_)
        req.execution_context.hash = str(bstack1l1lllll1ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1lllll1ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1lllll1ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1lll1ll1l1l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1lll1llllll_opy_)
            log_entry.uuid = entry.bstack1ll11l1l11l_opy_
            log_entry.test_framework_state = bstack1l1lllll1ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lllll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᗥ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1lllll1_opy_ (u"ࠨࠢᗦ")
            if entry.kind == bstack1lllll1_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᗧ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1ll11l_opy_
                log_entry.file_path = entry.bstack11l1l11_opy_
        def bstack1ll11l1l111_opy_():
            bstack1l11llll11_opy_ = datetime.now()
            try:
                self.bstack1111111l1l_opy_.LogCreatedEvent(req)
                bstack1l1lllll1ll_opy_.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᗨ"), datetime.now() - bstack1l11llll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࢁࡽࠣᗩ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll11l1l111_opy_)
    def __1l1lllll111_opy_(self, instance) -> None:
        bstack1lllll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡍࡱࡤࡨࡸࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡪࡧࡴࡦࡵࠣࡥࠥࡪࡩࡤࡶࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡩࡶࡴࡳࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡦࡴࡤࠡࡷࡳࡨࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡵࡷࡥࡹ࡫ࠠࡶࡵ࡬ࡲ࡬ࠦࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᗪ")
        bstack1ll111lll11_opy_ = {bstack1lllll1_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᗫ"): bstack1ll11l11ll1_opy_.bstack1ll111ll1ll_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11ll1111_opy_(instance, bstack1ll111lll11_opy_)
    @staticmethod
    def bstack1ll111l1l11_opy_(instance: bstack1lll1l11l11_opy_, bstack1l1llllll1l_opy_: str):
        bstack1ll11ll11l1_opy_ = (
            bstack1l1l1l111l1_opy_.bstack1ll1ll11111_opy_
            if bstack1l1llllll1l_opy_ == bstack1l1l1l111l1_opy_.bstack1ll1ll1111l_opy_
            else bstack1l1l1l111l1_opy_.bstack1ll1ll11l1l_opy_
        )
        bstack1ll1l1l1l1l_opy_ = TestFramework.get_state(instance, bstack1l1llllll1l_opy_, None)
        bstack1l1lllll11l_opy_ = TestFramework.get_state(instance, bstack1ll11ll11l1_opy_, None) if bstack1ll1l1l1l1l_opy_ else None
        return (
            bstack1l1lllll11l_opy_[bstack1ll1l1l1l1l_opy_][-1]
            if isinstance(bstack1l1lllll11l_opy_, dict) and len(bstack1l1lllll11l_opy_.get(bstack1ll1l1l1l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll111ll111_opy_(instance: bstack1lll1l11l11_opy_, bstack1l1llllll1l_opy_: str):
        hook = bstack1l1l1l111l1_opy_.bstack1ll111l1l11_opy_(instance, bstack1l1llllll1l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll111ll1l1_opy_, []).clear()
    @staticmethod
    def __1ll11llllll_opy_(instance: bstack1lll1l11l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1lllll1_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥᗬ"), None)):
            return
        if os.getenv(bstack1lllll1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥᗭ"), bstack1lllll1_opy_ (u"ࠢ࠲ࠤᗮ")) != bstack1lllll1_opy_ (u"ࠣ࠳ࠥᗯ"):
            bstack1l1l1l111l1_opy_.logger.warning(bstack1lllll1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦᗰ"))
            return
        bstack1l1lllllll1_opy_ = {
            bstack1lllll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᗱ"): (bstack1l1l1l111l1_opy_.bstack1ll111l1ll1_opy_, bstack1l1l1l111l1_opy_.bstack1ll1ll11l1l_opy_),
            bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᗲ"): (bstack1l1l1l111l1_opy_.bstack1ll1ll1111l_opy_, bstack1l1l1l111l1_opy_.bstack1ll1ll11111_opy_),
        }
        for when in (bstack1lllll1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᗳ"), bstack1lllll1_opy_ (u"ࠨࡣࡢ࡮࡯ࠦᗴ"), bstack1lllll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᗵ")):
            bstack1ll1111lll1_opy_ = args[1].get_records(when)
            if not bstack1ll1111lll1_opy_:
                continue
            records = [
                bstack1ll1l1l1ll1_opy_(
                    kind=TestFramework.bstack1ll11111111_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1lllll1_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦᗶ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1lllll1_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥᗷ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1111lll1_opy_
                if isinstance(getattr(r, bstack1lllll1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᗸ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l1llllll11_opy_, bstack1ll11ll11l1_opy_ = bstack1l1lllllll1_opy_.get(when, (None, None))
            bstack1ll1l1l1l11_opy_ = TestFramework.get_state(instance, bstack1l1llllll11_opy_, None) if bstack1l1llllll11_opy_ else None
            bstack1l1lllll11l_opy_ = TestFramework.get_state(instance, bstack1ll11ll11l1_opy_, None) if bstack1ll1l1l1l11_opy_ else None
            if isinstance(bstack1l1lllll11l_opy_, dict) and len(bstack1l1lllll11l_opy_.get(bstack1ll1l1l1l11_opy_, [])) > 0:
                hook = bstack1l1lllll11l_opy_[bstack1ll1l1l1l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll111ll1l1_opy_ in hook:
                    hook[TestFramework.bstack1ll111ll1l1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l1llll1_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l1l111l1_opy_.__1ll1l1lll11_opy_(test.location) if hasattr(test, bstack1lllll1_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᗹ")) else getattr(test, bstack1lllll1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᗺ"), None)
        test_name = test.name if hasattr(test, bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᗻ")) else None
        bstack1ll111l11l1_opy_ = test.fspath.strpath if hasattr(test, bstack1lllll1_opy_ (u"ࠢࡧࡵࡳࡥࡹ࡮ࠢᗼ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll111l11l1_opy_:
            return None
        code = None
        if hasattr(test, bstack1lllll1_opy_ (u"ࠣࡱࡥ࡮ࠧᗽ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll1llll_opy_ = []
        try:
            bstack11llll1llll_opy_ = bstack1llll111_opy_.bstack1l111l1l_opy_(test)
        except:
            bstack1l1l1l111l1_opy_.logger.warning(bstack1lllll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸࡪࡹࡴࠡࡵࡦࡳࡵ࡫ࡳ࠭ࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡴࡨࡷࡴࡲࡶࡦࡦࠣ࡭ࡳࠦࡃࡍࡋࠥᗾ"))
        return {
            TestFramework.bstack1lll1lllll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1l1lll_opy_: test_id,
            TestFramework.bstack1ll11l111ll_opy_: test_name,
            TestFramework.bstack1ll11ll1lll_opy_: getattr(test, bstack1lllll1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᗿ"), None),
            TestFramework.bstack1ll111111ll_opy_: bstack1ll111l11l1_opy_,
            TestFramework.bstack1ll11l11l1l_opy_: bstack1l1l1l111l1_opy_.__1ll1111ll11_opy_(test),
            TestFramework.bstack1ll1l111l11_opy_: code,
            TestFramework.bstack1lll1ll1111_opy_: TestFramework.bstack1ll111l11ll_opy_,
            TestFramework.bstack1lll11l1l11_opy_: test_id,
            TestFramework.bstack1l1111l1ll1_opy_: bstack11llll1llll_opy_
        }
    @staticmethod
    def __1ll1111ll11_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1lllll1_opy_ (u"ࠦࡴࡽ࡮ࡠ࡯ࡤࡶࡰ࡫ࡲࡴࠤᘀ"), [])
            markers.extend([getattr(m, bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘁ"), None) for m in own_markers if getattr(m, bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘂ"), None)])
            current = getattr(current, bstack1lllll1_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᘃ"), None)
        return markers
    @staticmethod
    def __1ll1l1lll11_opy_(location):
        return bstack1lllll1_opy_ (u"ࠣ࠼࠽ࠦᘄ").join(filter(lambda x: isinstance(x, str), location))