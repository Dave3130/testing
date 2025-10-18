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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack1lllll11l1l_opy_, bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1l1_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1llll1111l1_opy_, bstack1lll1ll111l_opy_, bstack1ll11l111l1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1l1ll1l_opy_, bstack1ll11ll1l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1l11l1_opy_ = [bstack11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᏔ"), bstack11ll_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᏕ"), bstack11ll_opy_ (u"ࠥࡧࡴࡴࡦࡪࡩࠥᏖ"), bstack11ll_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࠧᏗ"), bstack11ll_opy_ (u"ࠧࡶࡡࡵࡪࠥᏘ")]
bstack1ll1l1l1111_opy_ = bstack1ll11ll1l1l_opy_()
bstack1ll1l1111ll_opy_ = bstack11ll_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᏙ")
bstack1l11l11111l_opy_ = {
    bstack11ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡊࡶࡨࡱࠧᏚ"): bstack1l11l1l11l1_opy_,
    bstack11ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡒࡤࡧࡰࡧࡧࡦࠤᏛ"): bstack1l11l1l11l1_opy_,
    bstack11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡐࡳࡩࡻ࡬ࡦࠤᏜ"): bstack1l11l1l11l1_opy_,
    bstack11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡇࡱࡧࡳࡴࠤᏝ"): bstack1l11l1l11l1_opy_,
    bstack11ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡋࡻ࡮ࡤࡶ࡬ࡳࡳࠨᏞ"): bstack1l11l1l11l1_opy_
    + [
        bstack11ll_opy_ (u"ࠧࡵࡲࡪࡩ࡬ࡲࡦࡲ࡮ࡢ࡯ࡨࠦᏟ"),
        bstack11ll_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᏠ"),
        bstack11ll_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࡪࡰࡩࡳࠧᏡ"),
        bstack11ll_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᏢ"),
        bstack11ll_opy_ (u"ࠤࡦࡥࡱࡲࡳࡱࡧࡦࠦᏣ"),
        bstack11ll_opy_ (u"ࠥࡧࡦࡲ࡬ࡰࡤ࡭ࠦᏤ"),
        bstack11ll_opy_ (u"ࠦࡸࡺࡡࡳࡶࠥᏥ"),
        bstack11ll_opy_ (u"ࠧࡹࡴࡰࡲࠥᏦ"),
        bstack11ll_opy_ (u"ࠨࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠣᏧ"),
        bstack11ll_opy_ (u"ࠢࡸࡪࡨࡲࠧᏨ"),
    ],
    bstack11ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤ࡭ࡳ࠴ࡓࡦࡵࡶ࡭ࡴࡴࠢᏩ"): [bstack11ll_opy_ (u"ࠤࡶࡸࡦࡸࡴࡱࡣࡷ࡬ࠧᏪ"), bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡴࡨࡤ࡭ࡱ࡫ࡤࠣᏫ"), bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࡦࡳࡱࡲࡥࡤࡶࡨࡨࠧᏬ"), bstack11ll_opy_ (u"ࠧ࡯ࡴࡦ࡯ࡶࠦᏭ")],
    bstack11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡣࡰࡰࡩ࡭࡬࠴ࡃࡰࡰࡩ࡭࡬ࠨᏮ"): [bstack11ll_opy_ (u"ࠢࡪࡰࡹࡳࡨࡧࡴࡪࡱࡱࡣࡵࡧࡲࡢ࡯ࡶࠦᏯ"), bstack11ll_opy_ (u"ࠣࡣࡵ࡫ࡸࠨᏰ")],
    bstack11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡋ࡯ࡸࡵࡷࡵࡩࡉ࡫ࡦࠣᏱ"): [bstack11ll_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᏲ"), bstack11ll_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧᏳ"), bstack11ll_opy_ (u"ࠧ࡬ࡵ࡯ࡥࠥᏴ"), bstack11ll_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᏵ"), bstack11ll_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤ᏶"), bstack11ll_opy_ (u"ࠣ࡫ࡧࡷࠧ᏷")],
    bstack11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡘࡻࡢࡓࡧࡴࡹࡪࡹࡴࠣᏸ"): [bstack11ll_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣᏹ"), bstack11ll_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࠥᏺ"), bstack11ll_opy_ (u"ࠧࡶࡡࡳࡣࡰࡣ࡮ࡴࡤࡦࡺࠥᏻ")],
    bstack11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡲࡶࡰࡱࡩࡷ࠴ࡃࡢ࡮࡯ࡍࡳ࡬࡯ࠣᏼ"): [bstack11ll_opy_ (u"ࠢࡸࡪࡨࡲࠧᏽ"), bstack11ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࠣ᏾")],
    bstack11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥࡷࡱ࠮ࡴࡶࡵࡹࡨࡺࡵࡳࡧࡶ࠲ࡓࡵࡤࡦࡍࡨࡽࡼࡵࡲࡥࡵࠥ᏿"): [bstack11ll_opy_ (u"ࠥࡲࡴࡪࡥࠣ᐀"), bstack11ll_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᐁ")],
    bstack11ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡎࡣࡵ࡯ࠧᐂ"): [bstack11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐃ"), bstack11ll_opy_ (u"ࠢࡢࡴࡪࡷࠧᐄ"), bstack11ll_opy_ (u"ࠣ࡭ࡺࡥࡷ࡭ࡳࠣᐅ")],
}
_1ll1111ll1l_opy_ = set()
class bstack1l1l11l1ll1_opy_(bstack1lllllllll1_opy_):
    bstack1l11l1ll11l_opy_ = bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡧࡩࡩࡷࡸࡥࡥࠤᐆ")
    bstack1l11l1l11ll_opy_ = bstack11ll_opy_ (u"ࠥࡍࡓࡌࡏࠣᐇ")
    bstack1l11l11l1ll_opy_ = bstack11ll_opy_ (u"ࠦࡊࡘࡒࡐࡔࠥᐈ")
    bstack1l11l1ll1l1_opy_: Callable
    bstack1l11l111l1l_opy_: Callable
    def __init__(self, bstack1l1l11l1l11_opy_, bstack1ll1ll1l11l_opy_):
        super().__init__()
        self.bstack1l11ll11111_opy_ = bstack1ll1ll1l11l_opy_
        if os.getenv(bstack11ll_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡔ࠷࠱࡚ࠤᐉ"), bstack11ll_opy_ (u"ࠨ࠱ࠣᐊ")) != bstack11ll_opy_ (u"ࠢ࠲ࠤᐋ") or not self.is_enabled():
            self.logger.warning(bstack11ll_opy_ (u"ࠣࠤᐌ") + str(self.__class__.__name__) + bstack11ll_opy_ (u"ࠤࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠧᐍ"))
            return
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1lll1lll1l1_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l11lll_opy_)
        for event in bstack1lll1l1ll11_opy_:
            for state in bstack1lll1ll111l_opy_:
                TestFramework.bstack1lllll1l1ll_opy_((event, state), self.bstack1l11l11llll_opy_)
        bstack1l1l11l1l11_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.POST), self.bstack1l111llllll_opy_)
        self.bstack1l11l1ll1l1_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l1l1lll_opy_(bstack1l1l11l1ll1_opy_.bstack1l11l1l11ll_opy_, self.bstack1l11l1ll1l1_opy_)
        self.bstack1l11l111l1l_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l1l1lll_opy_(bstack1l1l11l1ll1_opy_.bstack1l11l11l1ll_opy_, self.bstack1l11l111l1l_opy_)
        self.bstack1l11l1lll1l_opy_ = builtins.print
        builtins.print = self.bstack1l11l111l11_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll1l1l111l_opy_() and instance:
            bstack1l11l11ll1l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1l11l_opy_
            if test_framework_state == bstack1lll1l1ll11_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG:
                bstack1l11111lll_opy_ = datetime.now()
                entries = f.bstack1ll11ll11ll_opy_(instance, bstack1lllll1l11l_opy_)
                if entries:
                    self.bstack1ll11l1l1l1_opy_(instance, entries)
                    instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࠥᐎ"), datetime.now() - bstack1l11111lll_opy_)
                    f.bstack1ll11llll11_opy_(instance, bstack1lllll1l11l_opy_)
                instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᐏ"), datetime.now() - bstack1l11l11ll1l_opy_)
                return # do not send this event with the bstack1l11l111111_opy_ bstack1l11l11l11l_opy_
            elif (
                test_framework_state == bstack1lll1l1ll11_opy_.TEST
                and test_hook_state == bstack1lll1ll111l_opy_.POST
                and not f.bstack1lllllll111_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_)
            ):
                self.logger.warning(bstack11ll_opy_ (u"ࠧࡪࡲࡰࡲࡳ࡭ࡳ࡭ࠠࡥࡷࡨࠤࡹࡵࠠ࡭ࡣࡦ࡯ࠥࡵࡦࠡࡴࡨࡷࡺࡲࡴࡴࠢࠥᐐ") + str(TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_)) + bstack11ll_opy_ (u"ࠨࠢᐑ"))
                f.bstack1llllll1lll_opy_(instance, bstack1l1l11l1ll1_opy_.bstack1l11l1ll11l_opy_, True)
                return # do not send this event bstack1l11l1lll11_opy_ bstack1l11l1l1l1l_opy_
            elif (
                f.get_state(instance, bstack1l1l11l1ll1_opy_.bstack1l11l1ll11l_opy_, False)
                and test_framework_state == bstack1lll1l1ll11_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1ll111l_opy_.POST
                and f.bstack1lllllll111_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_)
            ):
                self.logger.warning(bstack11ll_opy_ (u"ࠢࡪࡰ࡭ࡩࡨࡺࡩ࡯ࡩࠣࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡖࡈࡗ࡙࠲ࠠࡕࡧࡶࡸࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡑࡑࡖࡘࠥࠨᐒ") + str(TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1ll11l1ll11_opy_)) + bstack11ll_opy_ (u"ࠣࠤᐓ"))
                self.bstack1l11l11llll_opy_(f, instance, (bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), *args, **kwargs)
            bstack1l11111lll_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l11l1l1_opy_ = sorted(
                filter(lambda x: x.get(bstack11ll_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᐔ"), None), data.pop(bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᐕ"), {}).values()),
                key=lambda x: x[bstack11ll_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᐖ")],
            )
            if bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_ in data:
                data.pop(bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_)
            data.update({bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᐗ"): bstack1l11l11l1l1_opy_})
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᐘ"), datetime.now() - bstack1l11111lll_opy_)
            bstack1l11111lll_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l111lllll1_opy_)
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠢ࡫ࡵࡲࡲ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᐙ"), datetime.now() - bstack1l11111lll_opy_)
            self.bstack1l11l11l11l_opy_(instance, bstack1lllll1l11l_opy_, event_json=event_json)
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦᐚ"), datetime.now() - bstack1l11l11ll1l_opy_)
    def bstack1lll1lll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
        bstack1ll111l11ll_opy_ = bstack1llll11ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1l1l1l11ll_opy_.value)
        self.bstack1l11ll11111_opy_.bstack1lll1llll11_opy_(instance, f, bstack1lllll1l11l_opy_, *args, **kwargs)
        bstack1llll11ll11_opy_.end(EVENTS.bstack1l1l1l11ll_opy_.value, bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᐛ"), bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᐜ"), status=True, failure=None, test_name=None)
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11ll11111_opy_.bstack1lll1llll1l_opy_(instance, f, bstack1lllll1l11l_opy_, *args, **kwargs)
        self.bstack1l11l11l111_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l11ll11_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1l11l11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡗࡪࡹࡳࡪࡱࡱࡉࡻ࡫࡮ࡵࠢࡪࡖࡕࡉࠠࡤࡣ࡯ࡰ࠿ࠦࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠢᐝ"))
            return
        bstack1l11111lll_opy_ = datetime.now()
        try:
            r = self.bstack1lllll11111_opy_.TestSessionEvent(req)
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡦࡸࡨࡲࡹࠨᐞ"), datetime.now() - bstack1l11111lll_opy_)
            f.bstack1llllll1lll_opy_(instance, self.bstack1l11ll11111_opy_.bstack1lll1l1l11l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11ll_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᐟ") + str(r) + bstack11ll_opy_ (u"ࠢࠣᐠ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᐡ") + str(e) + bstack11ll_opy_ (u"ࠤࠥᐢ"))
            traceback.print_exc()
            raise e
    def bstack1l111llllll_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        _driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        _1l11l1llll1_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll1l1l1_opy_.bstack1l1ll1ll11l_opy_(method_name):
            return
        if f.bstack1l1lll11l11_opy_(*args) == bstack1lllll1l1l1_opy_.bstack1l11l11lll1_opy_:
            bstack1l11l11ll1l_opy_ = datetime.now()
            screenshot = result.get(bstack11ll_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤᐣ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11ll_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠢ࡬ࡱࡦ࡭ࡥࠡࡤࡤࡷࡪ࠼࠴ࠡࡵࡷࡶࠧᐤ"))
                return
            bstack1ll11l1llll_opy_ = self.bstack1l111llll1l_opy_(instance)
            if bstack1ll11l1llll_opy_:
                entry = bstack1ll11l111l1_opy_(TestFramework.bstack1l111lll11l_opy_, screenshot)
                self.bstack1ll11l1l1l1_opy_(bstack1ll11l1llll_opy_, [entry])
                instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡࡧࡶࡨࡶࡤ࡫ࡸࡦࡥࡸࡸࡪࠨᐥ"), datetime.now() - bstack1l11l11ll1l_opy_)
            else:
                self.logger.warning(bstack11ll_opy_ (u"ࠨࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡥࡴࡶࠣࡪࡴࡸࠠࡸࡪ࡬ࡧ࡭ࠦࡴࡩ࡫ࡶࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡࡹࡤࡷࠥࡺࡡ࡬ࡧࡱࠤࡧࡿࠠࡥࡴ࡬ࡺࡪࡸ࠽ࠡࡽࢀࠦᐦ").format(instance.ref()))
        event = {}
        bstack1ll11l1llll_opy_ = self.bstack1l111llll1l_opy_(instance)
        if bstack1ll11l1llll_opy_:
            self.bstack1l111ll1l1l_opy_(event, bstack1ll11l1llll_opy_)
            if event.get(bstack11ll_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᐧ")):
                self.bstack1ll11l1l1l1_opy_(bstack1ll11l1llll_opy_, event[bstack11ll_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᐨ")])
            else:
                self.logger.debug(bstack11ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡ࡮ࡲ࡫ࡸࠦࡦࡰࡴࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡦࡸࡨࡲࡹࠨᐩ"))
    @measure(event_name=EVENTS.bstack1l11l1111ll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1ll11l1l1l1_opy_(
        self,
        bstack1ll11l1llll_opy_: bstack1llll1111l1_opy_,
        entries: List[bstack1ll11l111l1_opy_],
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1llll1l111l_opy_)
        req.execution_context.hash = str(bstack1ll11l1llll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l1llll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l1llll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1lll1lllll1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1lll1l11111_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1llll111l11_opy_)
            log_entry.test_framework_state = bstack1ll11l1llll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᐪ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᐫ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111111ll_opy_
                log_entry.file_path = entry.bstack1lllll_opy_
        def bstack1ll11lll1l1_opy_():
            bstack1l11111lll_opy_ = datetime.now()
            try:
                self.bstack1lllll11111_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l111lll11l_opy_:
                    bstack1ll11l1llll_opy_.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᐬ"), datetime.now() - bstack1l11111lll_opy_)
                elif entry.kind == TestFramework.bstack1l11l1l1111_opy_:
                    bstack1ll11l1llll_opy_.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥᐭ"), datetime.now() - bstack1l11111lll_opy_)
                else:
                    bstack1ll11l1llll_opy_.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟࡭ࡱࡪࠦᐮ"), datetime.now() - bstack1l11111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᐯ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11lll1l1_opy_)
    @measure(event_name=EVENTS.bstack1l11l1lllll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1l11l11l11l_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        event_json=None,
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1lllll1l11l_opy_[0].name
        req.test_hook_state = bstack1lllll1l11l_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1l1lllll11l_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l111lllll1_opy_)).encode(bstack11ll_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᐰ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll11lll1l1_opy_():
            bstack1l11111lll_opy_ = datetime.now()
            try:
                self.bstack1lllll11111_opy_.TestFrameworkEvent(req)
                instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡦࡸࡨࡲࡹࠨᐱ"), datetime.now() - bstack1l11111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐲ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11lll1l1_opy_)
    def bstack1l111llll1l_opy_(self, instance: bstack1lllll11l1l_opy_):
        bstack1l111lll111_opy_ = TestFramework.bstack1l111ll1lll_opy_(instance.context)
        for t in bstack1l111lll111_opy_:
            bstack1lll1111l1l_opy_ = TestFramework.get_state(t, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l1l_opy_):
                return t
    def bstack1l11l1ll111_opy_(self, message):
        self.bstack1l11l1ll1l1_opy_(message + bstack11ll_opy_ (u"ࠧࡢ࡮ࠣᐳ"))
    def log_error(self, message):
        self.bstack1l11l111l1l_opy_(message + bstack11ll_opy_ (u"ࠨ࡜࡯ࠤᐴ"))
    def bstack1l11l1l1lll_opy_(self, level, original_func):
        def bstack1l111ll1ll1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11ll_opy_ (u"ࠢࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥࠣᐵ") in message or bstack11ll_opy_ (u"ࠣ࡝ࡖࡈࡐࡉࡌࡊ࡟ࠥᐶ") in message or bstack11ll_opy_ (u"ࠤ࡞࡛ࡪࡨࡄࡳ࡫ࡹࡩࡷࡓ࡯ࡥࡷ࡯ࡩࡢࠨᐷ") in message:
                return return_value
            bstack1l111lll111_opy_ = TestFramework.bstack1l111llll11_opy_()
            if not bstack1l111lll111_opy_:
                return return_value
            bstack1ll11l1llll_opy_ = next(
                (
                    instance
                    for instance in bstack1l111lll111_opy_
                    if TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1llll111l11_opy_)
                ),
                None,
            )
            if not bstack1ll11l1llll_opy_:
                return return_value
            entry = bstack1ll11l111l1_opy_(TestFramework.bstack1ll1l1l1l11_opy_, message, level)
            self.bstack1ll11l1l1l1_opy_(bstack1ll11l1llll_opy_, [entry])
            return return_value
        return bstack1l111ll1ll1_opy_
    def bstack1l11l111l11_opy_(self):
        def bstack1l11l111ll1_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1lll1l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11ll_opy_ (u"ࠪࠤࠬᐸ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11ll_opy_ (u"ࠦࡊࡼࡥ࡯ࡶࡇ࡭ࡸࡶࡡࡵࡥ࡫ࡩࡷࡓ࡯ࡥࡷ࡯ࡩࠧᐹ") in message:
                    return
                bstack1l111lll111_opy_ = TestFramework.bstack1l111llll11_opy_()
                if not bstack1l111lll111_opy_:
                    return
                bstack1ll11l1llll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l111lll111_opy_
                        if TestFramework.bstack1lllllll111_opy_(instance, TestFramework.bstack1llll111l11_opy_)
                    ),
                    None,
                )
                if not bstack1ll11l1llll_opy_:
                    return
                entry = bstack1ll11l111l1_opy_(TestFramework.bstack1ll1l1l1l11_opy_, message, bstack1l1l11l1ll1_opy_.bstack1l11l1l11ll_opy_)
                self.bstack1ll11l1l1l1_opy_(bstack1ll11l1llll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1lll1l_opy_(bstack11l1llll_opy_ (u"ࠧࡡࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫࡝ࠡࡎࡲ࡫ࠥࡩࡡࡱࡶࡸࡶࡪࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡦࡿࠥᐺ"))
                except:
                    pass
        return bstack1l11l111ll1_opy_
    def bstack1l111ll1l1l_opy_(self, event: dict, instance=None) -> None:
        global _1ll1111ll1l_opy_
        levels = [bstack11ll_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᐻ"), bstack11ll_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᐼ")]
        bstack1l11l111lll_opy_ = bstack11ll_opy_ (u"ࠣࠤᐽ")
        if instance is not None:
            try:
                bstack1l11l111lll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
            except Exception as e:
                self.logger.warning(bstack11ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡹ࡮ࡪࠠࡧࡴࡲࡱࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠢᐾ").format(e))
        bstack1l11l1l1l11_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᐿ")]
                bstack1ll11llll1l_opy_ = os.path.join(bstack1ll1l1l1111_opy_, (bstack1ll1l1111ll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll11llll1l_opy_):
                    self.logger.debug(bstack11ll_opy_ (u"ࠦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡯ࡱࡷࠤࡵࡸࡥࡴࡧࡱࡸࠥ࡬࡯ࡳࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡔࡦࡵࡷࠤࡦࡴࡤࠡࡄࡸ࡭ࡱࡪࠠ࡭ࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᑀ").format(bstack1ll11llll1l_opy_))
                    continue
                file_names = os.listdir(bstack1ll11llll1l_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll11llll1l_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1111ll1l_opy_:
                        self.logger.info(bstack11ll_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᑁ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l111lll1ll_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l111lll1ll_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11ll_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᑂ"):
                                entry = bstack1ll11l111l1_opy_(
                                    kind=bstack11ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᑃ"),
                                    message=bstack11ll_opy_ (u"ࠣࠤᑄ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll111111ll_opy_=file_size,
                                    bstack1ll11ll1l11_opy_=bstack11ll_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᑅ"),
                                    bstack1lllll_opy_=os.path.abspath(file_path),
                                    bstack1l11lllll_opy_=bstack1l11l111lll_opy_
                                )
                            elif level == bstack11ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᑆ"):
                                entry = bstack1ll11l111l1_opy_(
                                    kind=bstack11ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᑇ"),
                                    message=bstack11ll_opy_ (u"ࠧࠨᑈ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll111111ll_opy_=file_size,
                                    bstack1ll11ll1l11_opy_=bstack11ll_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᑉ"),
                                    bstack1lllll_opy_=os.path.abspath(file_path),
                                    bstack1ll111lll1l_opy_=bstack1l11l111lll_opy_
                                )
                            bstack1l11l1l1l11_opy_.append(entry)
                            _1ll1111ll1l_opy_.add(abs_path)
                        except Exception as bstack1l11l1111l1_opy_:
                            self.logger.error(bstack11ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡶࡦ࡯ࡳࡦࡦࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᑊ").format(bstack1l11l1111l1_opy_))
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡷࡧࡩࡴࡧࡧࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᑋ").format(e))
        event[bstack11ll_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᑌ")] = bstack1l11l1l1l11_opy_
class bstack1l111lllll1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11ll1111l_opy_ = set()
        kwargs[bstack11ll_opy_ (u"ࠥࡷࡰ࡯ࡰ࡬ࡧࡼࡷࠧᑍ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l1l111l_opy_(obj, self.bstack1l11ll1111l_opy_)
def bstack1l111lll1l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l1l111l_opy_(obj, bstack1l11ll1111l_opy_=None, max_depth=3):
    if bstack1l11ll1111l_opy_ is None:
        bstack1l11ll1111l_opy_ = set()
    if id(obj) in bstack1l11ll1111l_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11ll1111l_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l1ll1ll_opy_ = TestFramework.bstack1ll111l111l_opy_(obj)
    bstack1l11l1l1ll1_opy_ = next((k.lower() in bstack1l11l1ll1ll_opy_.lower() for k in bstack1l11l11111l_opy_.keys()), None)
    if bstack1l11l1l1ll1_opy_:
        obj = TestFramework.bstack1ll1l11lll1_opy_(obj, bstack1l11l11111l_opy_[bstack1l11l1l1ll1_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11ll_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢᑎ")):
            keys = getattr(obj, bstack11ll_opy_ (u"ࠧࡥ࡟ࡴ࡮ࡲࡸࡸࡥ࡟ࠣᑏ"), [])
        elif hasattr(obj, bstack11ll_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣᑐ")):
            keys = getattr(obj, bstack11ll_opy_ (u"ࠢࡠࡡࡧ࡭ࡨࡺ࡟ࡠࠤᑑ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11ll_opy_ (u"ࠣࡡࠥᑒ"))}
        if not obj and bstack1l11l1ll1ll_opy_ == bstack11ll_opy_ (u"ࠤࡳࡥࡹ࡮࡬ࡪࡤ࠱ࡔࡴࡹࡩࡹࡒࡤࡸ࡭ࠨᑓ"):
            obj = {bstack11ll_opy_ (u"ࠥࡴࡦࡺࡨࠣᑔ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l111lll1l1_opy_(key) or str(key).startswith(bstack11ll_opy_ (u"ࠦࡤࠨᑕ")):
            continue
        if value is not None and bstack1l111lll1l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l1l111l_opy_(value, bstack1l11ll1111l_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l1l111l_opy_(o, bstack1l11ll1111l_opy_, max_depth) for o in value]))
    return result or None