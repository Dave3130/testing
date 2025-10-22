# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll111l1_opy_, bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1l1llll_opy_, bstack1lll1lll111_opy_, bstack1ll1l1l1ll1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll11ll_opy_, bstack1ll1l1ll11l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l111l1l_opy_ = [bstack1lllll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᏐ"), bstack1lllll1l_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᏑ"), bstack1lllll1l_opy_ (u"ࠨࡣࡰࡰࡩ࡭࡬ࠨᏒ"), bstack1lllll1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࠣᏓ"), bstack1lllll1l_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᏔ")]
bstack1ll11ll1111_opy_ = bstack1ll1l1ll11l_opy_()
bstack1ll11lll11l_opy_ = bstack1lllll1l_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤᏕ")
bstack1l11l1l1111_opy_ = {
    bstack1lllll1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡍࡹ࡫࡭ࠣᏖ"): bstack1l11l111l1l_opy_,
    bstack1lllll1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡕࡧࡣ࡬ࡣࡪࡩࠧᏗ"): bstack1l11l111l1l_opy_,
    bstack1lllll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡓ࡯ࡥࡷ࡯ࡩࠧᏘ"): bstack1l11l111l1l_opy_,
    bstack1lllll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡃ࡭ࡣࡶࡷࠧᏙ"): bstack1l11l111l1l_opy_,
    bstack1lllll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡇࡷࡱࡧࡹ࡯࡯࡯ࠤᏚ"): bstack1l11l111l1l_opy_
    + [
        bstack1lllll1l_opy_ (u"ࠣࡱࡵ࡭࡬࡯࡮ࡢ࡮ࡱࡥࡲ࡫ࠢᏛ"),
        bstack1lllll1l_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦᏜ"),
        bstack1lllll1l_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨ࡭ࡳ࡬࡯ࠣᏝ"),
        bstack1lllll1l_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᏞ"),
        bstack1lllll1l_opy_ (u"ࠧࡩࡡ࡭࡮ࡶࡴࡪࡩࠢᏟ"),
        bstack1lllll1l_opy_ (u"ࠨࡣࡢ࡮࡯ࡳࡧࡰࠢᏠ"),
        bstack1lllll1l_opy_ (u"ࠢࡴࡶࡤࡶࡹࠨᏡ"),
        bstack1lllll1l_opy_ (u"ࠣࡵࡷࡳࡵࠨᏢ"),
        bstack1lllll1l_opy_ (u"ࠤࡧࡹࡷࡧࡴࡪࡱࡱࠦᏣ"),
        bstack1lllll1l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᏤ"),
    ],
    bstack1lllll1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡩ࡯࠰ࡖࡩࡸࡹࡩࡰࡰࠥᏥ"): [bstack1lllll1l_opy_ (u"ࠧࡹࡴࡢࡴࡷࡴࡦࡺࡨࠣᏦ"), bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡷ࡫ࡧࡩ࡭ࡧࡧࠦᏧ"), bstack1lllll1l_opy_ (u"ࠢࡵࡧࡶࡸࡸࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣᏨ"), bstack1lllll1l_opy_ (u"ࠣ࡫ࡷࡩࡲࡹࠢᏩ")],
    bstack1lllll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡦࡳࡳ࡬ࡩࡨ࠰ࡆࡳࡳ࡬ࡩࡨࠤᏪ"): [bstack1lllll1l_opy_ (u"ࠥ࡭ࡳࡼ࡯ࡤࡣࡷ࡭ࡴࡴ࡟ࡱࡣࡵࡥࡲࡹࠢᏫ"), bstack1lllll1l_opy_ (u"ࠦࡦࡸࡧࡴࠤᏬ")],
    bstack1lllll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡇ࡫ࡻࡸࡺࡸࡥࡅࡧࡩࠦᏭ"): [bstack1lllll1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᏮ"), bstack1lllll1l_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᏯ"), bstack1lllll1l_opy_ (u"ࠣࡨࡸࡲࡨࠨᏰ"), bstack1lllll1l_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᏱ"), bstack1lllll1l_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᏲ"), bstack1lllll1l_opy_ (u"ࠦ࡮ࡪࡳࠣᏳ")],
    bstack1lllll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡔࡷࡥࡖࡪࡷࡵࡦࡵࡷࠦᏴ"): [bstack1lllll1l_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᏵ"), bstack1lllll1l_opy_ (u"ࠢࡱࡣࡵࡥࡲࠨ᏶"), bstack1lllll1l_opy_ (u"ࠣࡲࡤࡶࡦࡳ࡟ࡪࡰࡧࡩࡽࠨ᏷")],
    bstack1lllll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡵࡹࡳࡴࡥࡳ࠰ࡆࡥࡱࡲࡉ࡯ࡨࡲࠦᏸ"): [bstack1lllll1l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᏹ"), bstack1lllll1l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࠦᏺ")],
    bstack1lllll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡏࡱࡧࡩࡐ࡫ࡹࡸࡱࡵࡨࡸࠨᏻ"): [bstack1lllll1l_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᏼ"), bstack1lllll1l_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᏽ")],
    bstack1lllll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡑࡦࡸ࡫ࠣ᏾"): [bstack1lllll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᏿"), bstack1lllll1l_opy_ (u"ࠥࡥࡷ࡭ࡳࠣ᐀"), bstack1lllll1l_opy_ (u"ࠦࡰࡽࡡࡳࡩࡶࠦᐁ")],
}
_1ll111l11l1_opy_ = set()
class bstack1l1l111llll_opy_(bstack1lllll1111l_opy_):
    bstack1l11l1llll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡪ࡬ࡥࡳࡴࡨࡨࠧᐂ")
    bstack1l11l11lll1_opy_ = bstack1lllll1l_opy_ (u"ࠨࡉࡏࡈࡒࠦᐃ")
    bstack1l11l1lll1l_opy_ = bstack1lllll1l_opy_ (u"ࠢࡆࡔࡕࡓࡗࠨᐄ")
    bstack1l11l111l11_opy_: Callable
    bstack1l111llll1l_opy_: Callable
    def __init__(self, bstack1l11ll1l1ll_opy_, bstack1ll1ll1l111_opy_):
        super().__init__()
        self.bstack1l11l1111l1_opy_ = bstack1ll1ll1l111_opy_
        if os.getenv(bstack1lllll1l_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡐ࠳࠴࡝ࠧᐅ"), bstack1lllll1l_opy_ (u"ࠤ࠴ࠦᐆ")) != bstack1lllll1l_opy_ (u"ࠥ࠵ࠧᐇ") or not self.is_enabled():
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠦࠧᐈ") + str(self.__class__.__name__) + bstack1lllll1l_opy_ (u"ࠧࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠣᐉ"))
            return
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.PRE), self.bstack1lll1ll1111_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), self.bstack1lll1l11l11_opy_)
        for event in bstack1llll111l1l_opy_:
            for state in bstack1lll1lll111_opy_:
                TestFramework.bstack1llll1l1l11_opy_((event, state), self.bstack1l111ll1lll_opy_)
        bstack1l11ll1l1ll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.POST), self.bstack1l11l11l1ll_opy_)
        self.bstack1l11l111l11_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l11l11l_opy_(bstack1l1l111llll_opy_.bstack1l11l11lll1_opy_, self.bstack1l11l111l11_opy_)
        self.bstack1l111llll1l_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l11l11l_opy_(bstack1l1l111llll_opy_.bstack1l11l1lll1l_opy_, self.bstack1l111llll1l_opy_)
        self.bstack1l11l111ll1_opy_ = builtins.print
        builtins.print = self.bstack1l11l1l1lll_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l111ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1l1lllll1ll_opy_() and instance:
            bstack1l111ll1ll1_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llll1l1lll_opy_
            if test_framework_state == bstack1llll111l1l_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll111l1l_opy_.LOG:
                bstack1ll111ll1_opy_ = datetime.now()
                entries = f.bstack1ll11ll1ll1_opy_(instance, bstack1llll1l1lll_opy_)
                if entries:
                    self.bstack1ll111l1111_opy_(instance, entries)
                    instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࠨᐊ"), datetime.now() - bstack1ll111ll1_opy_)
                    f.bstack1l1llll11l1_opy_(instance, bstack1llll1l1lll_opy_)
                instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᐋ"), datetime.now() - bstack1l111ll1ll1_opy_)
                return # do not send this event with the bstack1l111lll11l_opy_ bstack1l11l1l11l1_opy_
            elif (
                test_framework_state == bstack1llll111l1l_opy_.TEST
                and test_hook_state == bstack1lll1lll111_opy_.POST
                and not f.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11llll11_opy_)
            ):
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠣࡦࡵࡳࡵࡶࡩ࡯ࡩࠣࡨࡺ࡫ࠠࡵࡱࠣࡰࡦࡩ࡫ࠡࡱࡩࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࠨᐌ") + str(TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11llll11_opy_)) + bstack1lllll1l_opy_ (u"ࠤࠥᐍ"))
                f.bstack1llll11ll1l_opy_(instance, bstack1l1l111llll_opy_.bstack1l11l1llll1_opy_, True)
                return # do not send this event bstack1l11l1ll11l_opy_ bstack1l11l1l1ll1_opy_
            elif (
                f.get_state(instance, bstack1l1l111llll_opy_.bstack1l11l1llll1_opy_, False)
                and test_framework_state == bstack1llll111l1l_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1lll111_opy_.POST
                and f.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11llll11_opy_)
            ):
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠥ࡭ࡳࡰࡥࡤࡶ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲࡙ࡋࡓࡕ࠮ࠣࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡔࡔ࡙ࡔࠡࠤᐎ") + str(TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11llll11_opy_)) + bstack1lllll1l_opy_ (u"ࠦࠧᐏ"))
                self.bstack1l111ll1lll_opy_(f, instance, (bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), *args, **kwargs)
            bstack1ll111ll1_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1ll1l1_opy_ = sorted(
                filter(lambda x: x.get(bstack1lllll1l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᐐ"), None), data.pop(bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᐑ"), {}).values()),
                key=lambda x: x[bstack1lllll1l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᐒ")],
            )
            if bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_ in data:
                data.pop(bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_)
            data.update({bstack1lllll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᐓ"): bstack1l11l1ll1l1_opy_})
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᐔ"), datetime.now() - bstack1ll111ll1_opy_)
            bstack1ll111ll1_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l11ll11_opy_)
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠥ࡮ࡸࡵ࡮࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᐕ"), datetime.now() - bstack1ll111ll1_opy_)
            self.bstack1l11l1l11l1_opy_(instance, bstack1llll1l1lll_opy_, event_json=event_json)
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᐖ"), datetime.now() - bstack1l111ll1ll1_opy_)
    def bstack1lll1ll1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
        bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack1l11l1l1l_opy_.value)
        self.bstack1l11l1111l1_opy_.bstack1lll1l11ll1_opy_(instance, f, bstack1llll1l1lll_opy_, *args, **kwargs)
        bstack1llllllll1l_opy_.end(EVENTS.bstack1l11l1l1l_opy_.value, bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᐗ"), bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᐘ"), status=True, failure=None, test_name=None)
    def bstack1lll1l11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l1111l1_opy_.bstack1lll1l11l1l_opy_(instance, f, bstack1llll1l1lll_opy_, *args, **kwargs)
        self.bstack1l11l1lll11_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l111lllll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1l11l1lll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡗࡩࡸࡺࡓࡦࡵࡶ࡭ࡴࡴࡅࡷࡧࡱࡸࠥ࡭ࡒࡑࡅࠣࡧࡦࡲ࡬࠻ࠢࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠥᐙ"))
            return
        bstack1ll111ll1_opy_ = datetime.now()
        try:
            r = self.bstack1lllllll111_opy_.TestSessionEvent(req)
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡩࡻ࡫࡮ࡵࠤᐚ"), datetime.now() - bstack1ll111ll1_opy_)
            f.bstack1llll11ll1l_opy_(instance, self.bstack1l11l1111l1_opy_.bstack1lll1l11lll_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1lllll1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᐛ") + str(r) + bstack1lllll1l_opy_ (u"ࠥࠦᐜ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐝ") + str(e) + bstack1lllll1l_opy_ (u"ࠧࠨᐞ"))
            traceback.print_exc()
            raise e
    def bstack1l11l11l1ll_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        _driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        _1l11l1ll1ll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llll1lllll_opy_.bstack1l1lll11l11_opy_(method_name):
            return
        if f.bstack1l1ll1ll1l1_opy_(*args) == bstack1llll1lllll_opy_.bstack1l11ll111l1_opy_:
            bstack1l111ll1ll1_opy_ = datetime.now()
            screenshot = result.get(bstack1lllll1l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᐟ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠥ࡯࡭ࡢࡩࡨࠤࡧࡧࡳࡦ࠸࠷ࠤࡸࡺࡲࠣᐠ"))
                return
            bstack1ll11ll11ll_opy_ = self.bstack1l11l11l111_opy_(instance)
            if bstack1ll11ll11ll_opy_:
                entry = bstack1ll1l1l1ll1_opy_(TestFramework.bstack1l11l1l1l11_opy_, screenshot)
                self.bstack1ll111l1111_opy_(bstack1ll11ll11ll_opy_, [entry])
                instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡧࡻࡩࡨࡻࡴࡦࠤᐡ"), datetime.now() - bstack1l111ll1ll1_opy_)
            else:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠤࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶࡨࡷࡹࠦࡦࡰࡴࠣࡻ࡭࡯ࡣࡩࠢࡷ࡬࡮ࡹࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤࡼࡧࡳࠡࡶࡤ࡯ࡪࡴࠠࡣࡻࠣࡨࡷ࡯ࡶࡦࡴࡀࠤࢀࢃࠢᐢ").format(instance.ref()))
        event = {}
        bstack1ll11ll11ll_opy_ = self.bstack1l11l11l111_opy_(instance)
        if bstack1ll11ll11ll_opy_:
            self.bstack1l11l111111_opy_(event, bstack1ll11ll11ll_opy_)
            if event.get(bstack1lllll1l_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᐣ")):
                self.bstack1ll111l1111_opy_(bstack1ll11ll11ll_opy_, event[bstack1lllll1l_opy_ (u"ࠦࡱࡵࡧࡴࠤᐤ")])
            else:
                self.logger.debug(bstack1lllll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡱࡵࡧࡴࠢࡩࡳࡷࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡩࡻ࡫࡮ࡵࠤᐥ"))
    @measure(event_name=EVENTS.bstack1l11l11llll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1ll111l1111_opy_(
        self,
        bstack1ll11ll11ll_opy_: bstack1lll1l1llll_opy_,
        entries: List[bstack1ll1l1l1ll1_opy_],
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1llllllllll_opy_)
        req.execution_context.hash = str(bstack1ll11ll11ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll11ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll11ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll1l111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll11lll11_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll1lll1ll_opy_)
            log_entry.test_framework_state = bstack1ll11ll11ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lllll1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᐦ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1lllll1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᐧ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1l111_opy_
                log_entry.file_path = entry.bstack111l1l1_opy_
        def bstack1ll111lll11_opy_():
            bstack1ll111ll1_opy_ = datetime.now()
            try:
                self.bstack1lllllll111_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1l1l11_opy_:
                    bstack1ll11ll11ll_opy_.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᐨ"), datetime.now() - bstack1ll111ll1_opy_)
                elif entry.kind == TestFramework.bstack1l11l1lllll_opy_:
                    bstack1ll11ll11ll_opy_.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᐩ"), datetime.now() - bstack1ll111ll1_opy_)
                else:
                    bstack1ll11ll11ll_opy_.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡰࡴ࡭ࠢᐪ"), datetime.now() - bstack1ll111ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐫ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l11_opy_.enqueue(bstack1ll111lll11_opy_)
    @measure(event_name=EVENTS.bstack1l111lll111_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1l11l1l11l1_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        event_json=None,
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllllll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11lll11_opy_)
        req.test_framework_state = bstack1llll1l1lll_opy_[0].name
        req.test_hook_state = bstack1llll1l1lll_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11l1lll1_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l11l1ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l11ll11_opy_)).encode(bstack1lllll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᐬ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll111lll11_opy_():
            bstack1ll111ll1_opy_ = datetime.now()
            try:
                self.bstack1lllllll111_opy_.TestFrameworkEvent(req)
                instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡩࡻ࡫࡮ࡵࠤᐭ"), datetime.now() - bstack1ll111ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐮ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l11_opy_.enqueue(bstack1ll111lll11_opy_)
    def bstack1l11l11l111_opy_(self, instance: bstack1lllll111l1_opy_):
        bstack1l11ll1111l_opy_ = TestFramework.bstack1l11l111lll_opy_(instance.context)
        for t in bstack1l11ll1111l_opy_:
            bstack1lll1111l11_opy_ = TestFramework.get_state(t, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l11_opy_):
                return t
    def bstack1l11l11ll1l_opy_(self, message):
        self.bstack1l11l111l11_opy_(message + bstack1lllll1l_opy_ (u"ࠣ࡞ࡱࠦᐯ"))
    def log_error(self, message):
        self.bstack1l111llll1l_opy_(message + bstack1lllll1l_opy_ (u"ࠤ࡟ࡲࠧᐰ"))
    def bstack1l11l11l11l_opy_(self, level, original_func):
        def bstack1l11l11l1l1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1lllll1l_opy_ (u"ࠥࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࠦᐱ") in message or bstack1lllll1l_opy_ (u"ࠦࡠ࡙ࡄࡌࡅࡏࡍࡢࠨᐲ") in message or bstack1lllll1l_opy_ (u"ࠧࡡࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࡏࡲࡨࡺࡲࡥ࡞ࠤᐳ") in message:
                return return_value
            bstack1l11ll1111l_opy_ = TestFramework.bstack1l11l11111l_opy_()
            if not bstack1l11ll1111l_opy_:
                return return_value
            bstack1ll11ll11ll_opy_ = next(
                (
                    instance
                    for instance in bstack1l11ll1111l_opy_
                    if TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1lll1lll1ll_opy_)
                ),
                None,
            )
            if not bstack1ll11ll11ll_opy_:
                return return_value
            entry = bstack1ll1l1l1ll1_opy_(TestFramework.bstack1ll1l111l1l_opy_, message, level)
            self.bstack1ll111l1111_opy_(bstack1ll11ll11ll_opy_, [entry])
            return return_value
        return bstack1l11l11l1l1_opy_
    def bstack1l11l1l1lll_opy_(self):
        def bstack1l11l1111ll_opy_(*args, **kwargs):
            try:
                self.bstack1l11l111ll1_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1lllll1l_opy_ (u"࠭ࠠࠨᐴ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1lllll1l_opy_ (u"ࠢࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥࠣᐵ") in message:
                    return
                bstack1l11ll1111l_opy_ = TestFramework.bstack1l11l11111l_opy_()
                if not bstack1l11ll1111l_opy_:
                    return
                bstack1ll11ll11ll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11ll1111l_opy_
                        if TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1lll1lll1ll_opy_)
                    ),
                    None,
                )
                if not bstack1ll11ll11ll_opy_:
                    return
                entry = bstack1ll1l1l1ll1_opy_(TestFramework.bstack1ll1l111l1l_opy_, message, bstack1l1l111llll_opy_.bstack1l11l11lll1_opy_)
                self.bstack1ll111l1111_opy_(bstack1ll11ll11ll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l111ll1_opy_(bstack11ll1l1l_opy_ (u"ࠣ࡝ࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࡠࠤࡑࡵࡧࠡࡥࡤࡴࡹࡻࡲࡦࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࡩࢂࠨᐶ"))
                except:
                    pass
        return bstack1l11l1111ll_opy_
    def bstack1l11l111111_opy_(self, event: dict, instance=None) -> None:
        global _1ll111l11l1_opy_
        levels = [bstack1lllll1l_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᐷ"), bstack1lllll1l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᐸ")]
        bstack1l11l1l11ll_opy_ = bstack1lllll1l_opy_ (u"ࠦࠧᐹ")
        if instance is not None:
            try:
                bstack1l11l1l11ll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
            except Exception as e:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡻࡵࡪࡦࠣࡪࡷࡵ࡭ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠥᐺ").format(e))
        bstack1l11l1ll111_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᐻ")]
                bstack1ll1l11l11l_opy_ = os.path.join(bstack1ll11ll1111_opy_, (bstack1ll11lll11l_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1l11l11l_opy_):
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡲࡴࡺࠠࡱࡴࡨࡷࡪࡴࡴࠡࡨࡲࡶࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡗࡩࡸࡺࠠࡢࡰࡧࠤࡇࡻࡩ࡭ࡦࠣࡰࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᐼ").format(bstack1ll1l11l11l_opy_))
                    continue
                file_names = os.listdir(bstack1ll1l11l11l_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1l11l11l_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll111l11l1_opy_:
                        self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᐽ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l111llllll_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l111llllll_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1lllll1l_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᐾ"):
                                entry = bstack1ll1l1l1ll1_opy_(
                                    kind=bstack1lllll1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐿ"),
                                    message=bstack1lllll1l_opy_ (u"ࠦࠧᑀ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11l1l111_opy_=file_size,
                                    bstack1ll1l1l11l1_opy_=bstack1lllll1l_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᑁ"),
                                    bstack111l1l1_opy_=os.path.abspath(file_path),
                                    bstack11111l11l_opy_=bstack1l11l1l11ll_opy_
                                )
                            elif level == bstack1lllll1l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᑂ"):
                                entry = bstack1ll1l1l1ll1_opy_(
                                    kind=bstack1lllll1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᑃ"),
                                    message=bstack1lllll1l_opy_ (u"ࠣࠤᑄ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11l1l111_opy_=file_size,
                                    bstack1ll1l1l11l1_opy_=bstack1lllll1l_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᑅ"),
                                    bstack111l1l1_opy_=os.path.abspath(file_path),
                                    bstack1l1lllllll1_opy_=bstack1l11l1l11ll_opy_
                                )
                            bstack1l11l1ll111_opy_.append(entry)
                            _1ll111l11l1_opy_.add(abs_path)
                        except Exception as bstack1l11l1l1l1l_opy_:
                            self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡲࡢ࡫ࡶࡩࡩࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᑆ").format(bstack1l11l1l1l1l_opy_))
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡳࡣ࡬ࡷࡪࡪࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᑇ").format(e))
        event[bstack1lllll1l_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᑈ")] = bstack1l11l1ll111_opy_
class bstack1l11l11ll11_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11ll11111_opy_ = set()
        kwargs[bstack1lllll1l_opy_ (u"ࠨࡳ࡬࡫ࡳ࡯ࡪࡿࡳࠣᑉ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l1l111l_opy_(obj, self.bstack1l11ll11111_opy_)
def bstack1l111lll1l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l1l111l_opy_(obj, bstack1l11ll11111_opy_=None, max_depth=3):
    if bstack1l11ll11111_opy_ is None:
        bstack1l11ll11111_opy_ = set()
    if id(obj) in bstack1l11ll11111_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11ll11111_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l111lll1ll_opy_ = TestFramework.bstack1ll11ll1l1l_opy_(obj)
    bstack1l111llll11_opy_ = next((k.lower() in bstack1l111lll1ll_opy_.lower() for k in bstack1l11l1l1111_opy_.keys()), None)
    if bstack1l111llll11_opy_:
        obj = TestFramework.bstack1ll11l111ll_opy_(obj, bstack1l11l1l1111_opy_[bstack1l111llll11_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1lllll1l_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥᑊ")):
            keys = getattr(obj, bstack1lllll1l_opy_ (u"ࠣࡡࡢࡷࡱࡵࡴࡴࡡࡢࠦᑋ"), [])
        elif hasattr(obj, bstack1lllll1l_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦᑌ")):
            keys = getattr(obj, bstack1lllll1l_opy_ (u"ࠥࡣࡤࡪࡩࡤࡶࡢࡣࠧᑍ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1lllll1l_opy_ (u"ࠦࡤࠨᑎ"))}
        if not obj and bstack1l111lll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠧࡶࡡࡵࡪ࡯࡭ࡧ࠴ࡐࡰࡵ࡬ࡼࡕࡧࡴࡩࠤᑏ"):
            obj = {bstack1lllll1l_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᑐ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l111lll1l1_opy_(key) or str(key).startswith(bstack1lllll1l_opy_ (u"ࠢࡠࠤᑑ")):
            continue
        if value is not None and bstack1l111lll1l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l1l111l_opy_(value, bstack1l11ll11111_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l1l111l_opy_(o, bstack1l11ll11111_opy_, max_depth) for o in value]))
    return result or None