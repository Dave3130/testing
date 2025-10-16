# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
    bstack111111lll1_opy_,
    bstack1llll11l111_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1l1l_opy_, bstack11ll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lllll11ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_, bstack1llll1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1l1_opy_ import bstack1lll1l1llll_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11l111l1l1_opy_ import bstack11ll111ll1_opy_, bstack11l11lll1l_opy_, bstack1ll11l1l1_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1ll1lll_opy_(bstack1lll1l1llll_opy_):
    bstack1lll1l11l1l_opy_ = bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡸࡩࡷࡧࡵࡷࠧᄁ")
    bstack1lll1ll11l1_opy_ = bstack1ll11_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᄂ")
    bstack1lll1l11lll_opy_ = bstack1ll11_opy_ (u"ࠣࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᄃ")
    bstack1lll1l111l1_opy_ = bstack1ll11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᄄ")
    bstack1lll1lll11l_opy_ = bstack1ll11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡡࡵࡩ࡫ࡹࠢᄅ")
    bstack1lll1ll1111_opy_ = bstack1ll11_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥᄆ")
    bstack1lll1lll111_opy_ = bstack1ll11_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣᄇ")
    bstack1lll1l11l11_opy_ = bstack1ll11_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡸࡺࡡࡵࡷࡶࠦᄈ")
    def __init__(self):
        super().__init__(bstack1lll1llll11_opy_=self.bstack1lll1l11l1l_opy_, frameworks=[bstack1lllll11ll1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.BEFORE_EACH, bstack1lll1ll111l_opy_.POST), self.bstack1llll11lll1_opy_)
        if bstack11ll11lll1_opy_():
            TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1llll1l1111_opy_)
        else:
            TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1llll1l1111_opy_)
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll11lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        bstack1llll11111l_opy_ = self.bstack1llll111ll1_opy_(instance.context)
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡵࡧࡧࡦ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᄉ") + str(bstack1llll1l1ll1_opy_) + bstack1ll11_opy_ (u"ࠣࠤᄊ"))
            return
        f.bstack1llll1ll1ll_opy_(instance, bstack1lll1ll1lll_opy_.bstack1lll1ll11l1_opy_, bstack1llll11111l_opy_)
    def bstack1llll111ll1_opy_(self, context: bstack1llll11l111_opy_, bstack1llll11ll11_opy_= True):
        if bstack1llll11ll11_opy_:
            bstack1llll11111l_opy_ = self.bstack1lll1l1l1l1_opy_(context, reverse=True)
        else:
            bstack1llll11111l_opy_ = self.bstack1llll11llll_opy_(context, reverse=True)
        return [f for f in bstack1llll11111l_opy_ if f[1].state != bstack1lllllll1ll_opy_.QUIT]
    def bstack1llll1l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll11lll1_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄋ") + str(kwargs) + bstack1ll11_opy_ (u"ࠥࠦᄌ"))
            return
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1lll_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄍ") + str(kwargs) + bstack1ll11_opy_ (u"ࠧࠨᄎ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(
                bstack1lll1llllll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄏ"))
        bstack1lll1lll1l1_opy_, bstack1lll1lll1ll_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll1l1_opy_()
        if not page:
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄐ") + str(kwargs) + bstack1ll11_opy_ (u"ࠣࠤᄑ"))
            return
        bstack111ll11l1l_opy_ = getattr(args[0], bstack1ll11_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᄒ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll11_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᄓ")).get(bstack1ll11_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᄔ")):
            try:
                page.evaluate(bstack1ll11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᄕ"),
                            bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪᄖ") + json.dumps(
                                bstack111ll11l1l_opy_) + bstack1ll11_opy_ (u"ࠢࡾࡿࠥᄗ"))
            except Exception as e:
                self.logger.debug(bstack1ll11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨᄘ"), e)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll11lll1_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄙ") + str(kwargs) + bstack1ll11_opy_ (u"ࠥࠦᄚ"))
            return
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1lll_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄛ") + str(kwargs) + bstack1ll11_opy_ (u"ࠧࠨᄜ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(
                bstack1lll1llllll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄝ"))
        bstack1lll1lll1l1_opy_, bstack1lll1lll1ll_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll1l1_opy_()
        if not page:
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄞ") + str(kwargs) + bstack1ll11_opy_ (u"ࠣࠤᄟ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1llll1l_opy_, None)
        if not status:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᄠ") + str(bstack1llll1l1ll1_opy_) + bstack1ll11_opy_ (u"ࠥࠦᄡ"))
            return
        bstack1llll111111_opy_ = {bstack1ll11_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᄢ"): status.lower()}
        bstack1llll1l111l_opy_ = f.get_state(instance, TestFramework.bstack1llll11l11l_opy_, None)
        if status.lower() == bstack1ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᄣ") and bstack1llll1l111l_opy_ is not None:
            bstack1llll111111_opy_[bstack1ll11_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᄤ")] = bstack1llll1l111l_opy_[0][bstack1ll11_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᄥ")][0] if isinstance(bstack1llll1l111l_opy_, list) else str(bstack1llll1l111l_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᄦ")).get(bstack1ll11_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᄧ")):
            try:
                page.evaluate(
                        bstack1ll11_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄨ"),
                        bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࠩᄩ")
                        + json.dumps(bstack1llll111111_opy_)
                        + bstack1ll11_opy_ (u"ࠧࢃࠢᄪ")
                    )
            except Exception as e:
                self.logger.debug(bstack1ll11_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡿࢂࠨᄫ"), e)
    def bstack1lll1ll1ll1_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        f: TestFramework,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll11lll1_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(
                bstack1lll1llllll_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄬ"))
            return
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1lll_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄭ") + str(kwargs) + bstack1ll11_opy_ (u"ࠤࠥᄮ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(
                bstack1lll1llllll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᄯ"))
        bstack1lll1lll1l1_opy_, bstack1lll1lll1ll_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll1l1_opy_()
        if not page:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡲࡧࡲ࡬ࡡࡲ࠵࠶ࡿ࡟ࡴࡻࡱࡧ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄰ") + str(kwargs) + bstack1ll11_opy_ (u"ࠧࠨᄱ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1ll11_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦᄲ") + str(timestamp)
        try:
            page.evaluate(
                bstack1ll11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄳ"),
                bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ᄴ").format(
                    json.dumps(
                        {
                            bstack1ll11_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᄵ"): bstack1ll11_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᄶ"),
                            bstack1ll11_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᄷ"): {
                                bstack1ll11_opy_ (u"ࠧࡺࡹࡱࡧࠥᄸ"): bstack1ll11_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᄹ"),
                                bstack1ll11_opy_ (u"ࠢࡥࡣࡷࡥࠧᄺ"): data,
                                bstack1ll11_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᄻ"): bstack1ll11_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᄼ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1ll11_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦ࡯࠲࠳ࡼࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡾࢁࠧᄽ"), e)
    def bstack1llll1l11l1_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        f: TestFramework,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll11lll1_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1ll1lll_opy_.bstack1lll1ll1111_opy_, False):
            return
        self.bstack1111111l1l_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll111ll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1l1l11_opy_)
        req.test_framework_state = bstack1llll1l1ll1_opy_[0].name
        req.test_hook_state = bstack1llll1l1ll1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1l11ll1_opy_)
        for bstack1lll1l111ll_opy_ in bstack1llll1l11ll_opy_.bstack1llll1111l1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥᄾ")
                if bstack1lll1ll1l1l_opy_
                else bstack1ll11_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠦᄿ")
            )
            session.ref = bstack1lll1l111ll_opy_.ref()
            session.hub_url = bstack1llll1l11ll_opy_.get_state(bstack1lll1l111ll_opy_, bstack1llll1l11ll_opy_.bstack1lll1l1l1ll_opy_, bstack1ll11_opy_ (u"ࠨࠢᅀ"))
            session.framework_name = bstack1lll1l111ll_opy_.framework_name
            session.framework_version = bstack1lll1l111ll_opy_.framework_version
            session.framework_session_id = bstack1llll1l11ll_opy_.get_state(bstack1lll1l111ll_opy_, bstack1llll1l11ll_opy_.bstack1lll1ll1l11_opy_, bstack1ll11_opy_ (u"ࠢࠣᅁ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1ll11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1lll_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅂ") + str(kwargs) + bstack1ll11_opy_ (u"ࠤࠥᅃ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(bstack1ll11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅄ") + str(kwargs) + bstack1ll11_opy_ (u"ࠦࠧᅅ"))
        bstack1lll1lll1l1_opy_, bstack1lll1lll1ll_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll1l1_opy_()
        if not page:
            self.logger.debug(bstack1ll11_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅆ") + str(kwargs) + bstack1ll11_opy_ (u"ࠨࠢᅇ"))
            return
        return page
    def bstack1lll1lllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll111lll_opy_ = {}
        for bstack1lll1l111ll_opy_ in bstack1llll1l11ll_opy_.bstack1llll1111l1_opy_.values():
            caps = bstack1llll1l11ll_opy_.get_state(bstack1lll1l111ll_opy_, bstack1llll1l11ll_opy_.bstack1lll1l1lll1_opy_, bstack1ll11_opy_ (u"ࠢࠣᅈ"))
        bstack1llll111lll_opy_[bstack1ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨᅉ")] = caps.get(bstack1ll11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥᅊ"), bstack1ll11_opy_ (u"ࠥࠦᅋ"))
        bstack1llll111lll_opy_[bstack1ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᅌ")] = caps.get(bstack1ll11_opy_ (u"ࠧࡵࡳࠣᅍ"), bstack1ll11_opy_ (u"ࠨࠢᅎ"))
        bstack1llll111lll_opy_[bstack1ll11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᅏ")] = caps.get(bstack1ll11_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᅐ"), bstack1ll11_opy_ (u"ࠤࠥᅑ"))
        bstack1llll111lll_opy_[bstack1ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦᅒ")] = caps.get(bstack1ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᅓ"), bstack1ll11_opy_ (u"ࠧࠨᅔ"))
        return bstack1llll111lll_opy_
    def bstack1lll1l1l111_opy_(self, page: object, bstack1lll1l1ll11_opy_, args={}):
        try:
            bstack1lll1l1l11l_opy_ = bstack1ll11_opy_ (u"ࠨࠢࠣࠪࡩࡹࡳࡩࡴࡪࡱࡱࠤ࠭࠴࠮࠯ࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳࠪࠢࡾࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠ࡯ࡧࡺࠤࡕࡸ࡯࡮࡫ࡶࡩ࠭࠮ࡲࡦࡵࡲࡰࡻ࡫ࠬࠡࡴࡨ࡮ࡪࡩࡴࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡵࡷࡥࡨࡱࡓࡥ࡭ࡄࡶ࡬ࡹ࠮ࡱࡷࡶ࡬࠭ࡸࡥࡴࡱ࡯ࡺࡪ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡼࡨࡱࡣࡧࡵࡤࡺࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࡽࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭࠭ࢁࡡࡳࡩࡢ࡮ࡸࡵ࡮ࡾࠫࠥࠦࠧᅕ")
            bstack1lll1l1ll11_opy_ = bstack1lll1l1ll11_opy_.replace(bstack1ll11_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅖ"), bstack1ll11_opy_ (u"ࠣࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳࠣᅗ"))
            script = bstack1lll1l1l11l_opy_.format(fn_body=bstack1lll1l1ll11_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠤࡤ࠵࠶ࡿ࡟ࡴࡥࡵ࡭ࡵࡺ࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡈࡶࡷࡵࡲࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡹ࡮ࡥࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹ࠲ࠠࠣᅘ") + str(e) + bstack1ll11_opy_ (u"ࠥࠦᅙ"))