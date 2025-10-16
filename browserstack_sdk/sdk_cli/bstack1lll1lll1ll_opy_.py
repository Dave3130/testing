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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1111111l11_opy_,
    bstack1llll11l1l1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1l11l_opy_, bstack1ll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l1l_opy_ import bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l11_opy_ import bstack1lll1l1l111_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack111111ll1_opy_ import bstack111ll1111l_opy_, bstack1l1l1llll_opy_, bstack11lllll11_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1llll1l11ll_opy_(bstack1lll1l1l111_opy_):
    bstack1llll111111_opy_ = bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨᄂ")
    bstack1llll1111ll_opy_ = bstack1lllll1_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᄃ")
    bstack1lll1l111ll_opy_ = bstack1lllll1_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄄ")
    bstack1lll1lll111_opy_ = bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᄅ")
    bstack1lll1l11ll1_opy_ = bstack1lllll1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣᄆ")
    bstack1llll11llll_opy_ = bstack1lllll1_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᄇ")
    bstack1llll111l11_opy_ = bstack1lllll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᄈ")
    bstack1lll1ll11ll_opy_ = bstack1lllll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧᄉ")
    def __init__(self):
        super().__init__(bstack1lll1ll1lll_opy_=self.bstack1llll111111_opy_, frameworks=[bstack1lllll1ll11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.BEFORE_EACH, bstack1llll1l11l1_opy_.POST), self.bstack1lll1l11lll_opy_)
        if bstack1ll11llll1_opy_():
            TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1lll1l1lll1_opy_)
        else:
            TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1llll111lll_opy_ = self.bstack1llll11ll11_opy_(instance.context)
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡶࡡࡨࡧ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᄊ") + str(bstack1lllll111ll_opy_) + bstack1lllll1_opy_ (u"ࠤࠥᄋ"))
            return
        f.bstack1lllll1l11l_opy_(instance, bstack1llll1l11ll_opy_.bstack1llll1111ll_opy_, bstack1llll111lll_opy_)
    def bstack1llll11ll11_opy_(self, context: bstack1llll11l1l1_opy_, bstack1lll1lll1l1_opy_= True):
        if bstack1lll1lll1l1_opy_:
            bstack1llll111lll_opy_ = self.bstack1lll1ll111l_opy_(context, reverse=True)
        else:
            bstack1llll111lll_opy_ = self.bstack1lll1l1ll1l_opy_(context, reverse=True)
        return [f for f in bstack1llll111lll_opy_ if f[1].state != bstack1llll1ll1ll_opy_.QUIT]
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        if not bstack1lll1l1l11l_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄌ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠦࠧᄍ"))
            return
        bstack1llll111lll_opy_ = f.get_state(instance, bstack1llll1l11ll_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄎ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠨࠢᄏ"))
            return
        if len(bstack1llll111lll_opy_) > 1:
            self.logger.debug(
                bstack1lll1lll11l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄐ"))
        bstack1lll1l1l1ll_opy_, bstack1lll1ll11l1_opy_ = bstack1llll111lll_opy_[0]
        page = bstack1lll1l1l1ll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄑ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠤࠥᄒ"))
            return
        bstack1lllll1l11_opy_ = getattr(args[0], bstack1lllll1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᄓ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᄔ")).get(bstack1lllll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᄕ")):
            try:
                page.evaluate(bstack1lllll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᄖ"),
                            bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫᄗ") + json.dumps(
                                bstack1lllll1l11_opy_) + bstack1lllll1_opy_ (u"ࠣࡿࢀࠦᄘ"))
            except Exception as e:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢᄙ"), e)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        if not bstack1lll1l1l11l_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄚ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠦࠧᄛ"))
            return
        bstack1llll111lll_opy_ = f.get_state(instance, bstack1llll1l11ll_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄜ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠨࠢᄝ"))
            return
        if len(bstack1llll111lll_opy_) > 1:
            self.logger.debug(
                bstack1lll1lll11l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄞ"))
        bstack1lll1l1l1ll_opy_, bstack1lll1ll11l1_opy_ = bstack1llll111lll_opy_[0]
        page = bstack1lll1l1l1ll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄟ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠤࠥᄠ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1ll1111_opy_, None)
        if not status:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᄡ") + str(bstack1lllll111ll_opy_) + bstack1lllll1_opy_ (u"ࠦࠧᄢ"))
            return
        bstack1llll11ll1l_opy_ = {bstack1lllll1_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᄣ"): status.lower()}
        bstack1llll111ll1_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1llll_opy_, None)
        if status.lower() == bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᄤ") and bstack1llll111ll1_opy_ is not None:
            bstack1llll11ll1l_opy_[bstack1lllll1_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᄥ")] = bstack1llll111ll1_opy_[0][bstack1lllll1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᄦ")][0] if isinstance(bstack1llll111ll1_opy_, list) else str(bstack1llll111ll1_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᄧ")).get(bstack1lllll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᄨ")):
            try:
                page.evaluate(
                        bstack1lllll1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᄩ"),
                        bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࠪᄪ")
                        + json.dumps(bstack1llll11ll1l_opy_)
                        + bstack1lllll1_opy_ (u"ࠨࡽࠣᄫ")
                    )
            except Exception as e:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢᄬ"), e)
    def bstack1lll1llll1l_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        if not bstack1lll1l1l11l_opy_:
            self.logger.debug(
                bstack1lll1lll11l_opy_ (u"ࠣ࡯ࡤࡶࡰࡥ࡯࠲࠳ࡼࡣࡸࡿ࡮ࡤ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄭ"))
            return
        bstack1llll111lll_opy_ = f.get_state(instance, bstack1llll1l11ll_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄮ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠥࠦᄯ"))
            return
        if len(bstack1llll111lll_opy_) > 1:
            self.logger.debug(
                bstack1lll1lll11l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄰ"))
        bstack1lll1l1l1ll_opy_, bstack1lll1ll11l1_opy_ = bstack1llll111lll_opy_[0]
        page = bstack1lll1l1l1ll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄱ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠨࠢᄲ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1lllll1_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᄳ") + str(timestamp)
        try:
            page.evaluate(
                bstack1lllll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᄴ"),
                bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧᄵ").format(
                    json.dumps(
                        {
                            bstack1lllll1_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᄶ"): bstack1lllll1_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᄷ"),
                            bstack1lllll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᄸ"): {
                                bstack1lllll1_opy_ (u"ࠨࡴࡺࡲࡨࠦᄹ"): bstack1lllll1_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᄺ"),
                                bstack1lllll1_opy_ (u"ࠣࡦࡤࡸࡦࠨᄻ"): data,
                                bstack1lllll1_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᄼ"): bstack1lllll1_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᄽ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡰ࠳࠴ࡽࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡿࢂࠨᄾ"), e)
    def bstack1lll1ll1ll1_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1llll1l11ll_opy_.bstack1llll11llll_opy_, False):
            return
        self.bstack1llll1lllll_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1111111ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll1l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1llllll_opy_)
        req.test_framework_state = bstack1lllll111ll_opy_[0].name
        req.test_hook_state = bstack1lllll111ll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        for bstack1llll11111l_opy_ in bstack1lll1l1ll11_opy_.bstack1lll1llll11_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦᄿ")
                if bstack1lll1l1l11l_opy_
                else bstack1lllll1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠧᅀ")
            )
            session.ref = bstack1llll11111l_opy_.ref()
            session.hub_url = bstack1lll1l1ll11_opy_.get_state(bstack1llll11111l_opy_, bstack1lll1l1ll11_opy_.bstack1lll1l111l1_opy_, bstack1lllll1_opy_ (u"ࠢࠣᅁ"))
            session.framework_name = bstack1llll11111l_opy_.framework_name
            session.framework_version = bstack1llll11111l_opy_.framework_version
            session.framework_session_id = bstack1lll1l1ll11_opy_.get_state(bstack1llll11111l_opy_, bstack1lll1l1ll11_opy_.bstack1llll1l1l11_opy_, bstack1lllll1_opy_ (u"ࠣࠤᅂ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1llll11lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        bstack1llll111lll_opy_ = f.get_state(instance, bstack1llll1l11ll_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅃ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠥࠦᅄ"))
            return
        if len(bstack1llll111lll_opy_) > 1:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅅ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠧࠨᅆ"))
        bstack1lll1l1l1ll_opy_, bstack1lll1ll11l1_opy_ = bstack1llll111lll_opy_[0]
        page = bstack1lll1l1l1ll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅇ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠢࠣᅈ"))
            return
        return page
    def bstack1llll1l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll11l11l_opy_ = {}
        for bstack1llll11111l_opy_ in bstack1lll1l1ll11_opy_.bstack1lll1llll11_opy_.values():
            caps = bstack1lll1l1ll11_opy_.get_state(bstack1llll11111l_opy_, bstack1lll1l1ll11_opy_.bstack1llll11l111_opy_, bstack1lllll1_opy_ (u"ࠣࠤᅉ"))
        bstack1llll11l11l_opy_[bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢᅊ")] = caps.get(bstack1lllll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦᅋ"), bstack1lllll1_opy_ (u"ࠦࠧᅌ"))
        bstack1llll11l11l_opy_[bstack1lllll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᅍ")] = caps.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡴࠤᅎ"), bstack1lllll1_opy_ (u"ࠢࠣᅏ"))
        bstack1llll11l11l_opy_[bstack1lllll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᅐ")] = caps.get(bstack1lllll1_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᅑ"), bstack1lllll1_opy_ (u"ࠥࠦᅒ"))
        bstack1llll11l11l_opy_[bstack1lllll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧᅓ")] = caps.get(bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅔ"), bstack1lllll1_opy_ (u"ࠨࠢᅕ"))
        return bstack1llll11l11l_opy_
    def bstack1llll1l111l_opy_(self, page: object, bstack1llll1111l1_opy_, args={}):
        try:
            bstack1lll1l1l1l1_opy_ = bstack1lllll1_opy_ (u"ࠢࠣࠤࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࠮࠮࠯࠰ࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴࠫࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡰࡨࡻࠥࡖࡲࡰ࡯࡬ࡷࡪ࠮ࠨࡳࡧࡶࡳࡱࡼࡥ࠭ࠢࡵࡩ࡯࡫ࡣࡵࠫࠣࡁࡃࠦࡻࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳ࠯ࡲࡸࡷ࡭࠮ࡲࡦࡵࡲࡰࡻ࡫ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡽࡩࡲࡤࡨ࡯ࡥࡻࢀࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࢁ࠮࠮ࡻࡢࡴࡪࡣ࡯ࡹ࡯࡯ࡿࠬࠦࠧࠨᅖ")
            bstack1llll1111l1_opy_ = bstack1llll1111l1_opy_.replace(bstack1lllll1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅗ"), bstack1lllll1_opy_ (u"ࠤࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴࠤᅘ"))
            script = bstack1lll1l1l1l1_opy_.format(fn_body=bstack1llll1111l1_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠥࡥ࠶࠷ࡹࡠࡵࡦࡶ࡮ࡶࡴࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡉࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࠬࠡࠤᅙ") + str(e) + bstack1lllll1_opy_ (u"ࠦࠧᅚ"))