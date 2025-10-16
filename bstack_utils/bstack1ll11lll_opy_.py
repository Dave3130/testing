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
from uuid import uuid4
from bstack_utils.helper import bstack1llll11l_opy_, bstack111l1ll1lll_opy_
from bstack_utils.bstack1ll1l1lll1_opy_ import bstack11l11l11111_opy_
class bstack1l11l111_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111llll1_opy_=None, bstack111111lll1l_opy_=True, bstack1ll1111ll1l_opy_=None, bstack11ll1lll1l_opy_=None, result=None, duration=None, bstack1l11l11l_opy_=None, meta={}):
        self.bstack1l11l11l_opy_ = bstack1l11l11l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111lll1l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111llll1_opy_ = bstack111111llll1_opy_
        self.bstack1ll1111ll1l_opy_ = bstack1ll1111ll1l_opy_
        self.bstack11ll1lll1l_opy_ = bstack11ll1lll1l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack11llllll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1ll11_opy_(self, meta):
        self.meta = meta
    def bstack11ll11l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111ll1ll_opy_(self):
        bstack11111l11l1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬỨ"): bstack11111l11l1l_opy_,
            bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬứ"): bstack11111l11l1l_opy_,
            bstack1lllll1_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩỪ"): bstack11111l11l1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷ࠾ࠥࠨừ") + key)
            setattr(self, key, val)
    def bstack11111l11ll1_opy_(self):
        return {
            bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫỬ"): self.name,
            bstack1lllll1_opy_ (u"ࠧࡣࡱࡧࡽࠬử"): {
                bstack1lllll1_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭Ữ"): bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩữ"),
                bstack1lllll1_opy_ (u"ࠪࡧࡴࡪࡥࠨỰ"): self.code
            },
            bstack1lllll1_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫự"): self.scope,
            bstack1lllll1_opy_ (u"ࠬࡺࡡࡨࡵࠪỲ"): self.tags,
            bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩỳ"): self.framework,
            bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫỴ"): self.started_at
        }
    def bstack11111l1l1ll_opy_(self):
        return {
         bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭ỵ"): self.meta
        }
    def bstack11111l11lll_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬỶ"): {
                bstack1lllll1_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧỷ"): self.bstack111111llll1_opy_
            }
        }
    def bstack11111l1l1l1_opy_(self, bstack11111l111ll_opy_, details):
        step = next(filter(lambda st: st[bstack1lllll1_opy_ (u"ࠫ࡮ࡪࠧỸ")] == bstack11111l111ll_opy_, self.meta[bstack1lllll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫỹ")]), None)
        step.update(details)
    def bstack11ll1lll_opy_(self, bstack11111l111ll_opy_):
        step = next(filter(lambda st: st[bstack1lllll1_opy_ (u"࠭ࡩࡥࠩỺ")] == bstack11111l111ll_opy_, self.meta[bstack1lllll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ỻ")]), None)
        step.update({
            bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬỼ"): bstack1llll11l_opy_()
        })
    def bstack1ll11111_opy_(self, bstack11111l111ll_opy_, result, duration=None):
        bstack1ll1111ll1l_opy_ = bstack1llll11l_opy_()
        if bstack11111l111ll_opy_ is not None and self.meta.get(bstack1lllll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨỽ")):
            step = next(filter(lambda st: st[bstack1lllll1_opy_ (u"ࠪ࡭ࡩ࠭Ỿ")] == bstack11111l111ll_opy_, self.meta[bstack1lllll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỿ")]), None)
            step.update({
                bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪἀ"): bstack1ll1111ll1l_opy_,
                bstack1lllll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨἁ"): duration if duration else bstack111l1ll1lll_opy_(step[bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫἂ")], bstack1ll1111ll1l_opy_),
                bstack1lllll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨἃ"): result.result,
                bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪἄ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l1l11l_opy_):
        if self.meta.get(bstack1lllll1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἅ")):
            self.meta[bstack1lllll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἆ")].append(bstack11111l1l11l_opy_)
        else:
            self.meta[bstack1lllll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἇ")] = [ bstack11111l1l11l_opy_ ]
    def bstack11111l11l11_opy_(self):
        return {
            bstack1lllll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫἈ"): self.bstack11llllll_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack11111l1l1ll_opy_()
        }
    def bstack11111l111l1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬἉ"): self.bstack1ll1111ll1l_opy_,
            bstack1lllll1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩἊ"): self.duration,
            bstack1lllll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἋ"): self.result.result
        }
        if data[bstack1lllll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἌ")] == bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫἍ"):
            data[bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫἎ")] = self.result.bstack11111l11ll_opy_()
            data[bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧἏ")] = [{bstack1lllll1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪἐ"): self.result.bstack111l1l11l11_opy_()}]
        return data
    def bstack11111l1111l_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ἑ"): self.bstack11llllll_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack11111l111l1_opy_(),
            **self.bstack11111l1l1ll_opy_()
        }
    def bstack1lll11ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1lllll1_opy_ (u"ࠩࡖࡸࡦࡸࡴࡦࡦࠪἒ") in event:
            return self.bstack11111l11l11_opy_()
        elif bstack1lllll1_opy_ (u"ࠪࡊ࡮ࡴࡩࡴࡪࡨࡨࠬἓ") in event:
            return self.bstack11111l1111l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1111ll1l_opy_ = time if time else bstack1llll11l_opy_()
        self.duration = duration if duration else bstack111l1ll1lll_opy_(self.started_at, self.bstack1ll1111ll1l_opy_)
        if result:
            self.result = result
class bstack1lllll11_opy_(bstack1l11l111_opy_):
    def __init__(self, hooks=[], bstack1lll1111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1lll1111_opy_ = bstack1lll1111_opy_
        super().__init__(*args, **kwargs, bstack11ll1lll1l_opy_=bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࠩἔ"))
    @classmethod
    def bstack11111l11111_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lllll1_opy_ (u"ࠬ࡯ࡤࠨἕ"): id(step),
                bstack1lllll1_opy_ (u"࠭ࡴࡦࡺࡷࠫ἖"): step.name,
                bstack1lllll1_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨ἗"): step.keyword,
            })
        return bstack1lllll11_opy_(
            **kwargs,
            meta={
                bstack1lllll1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩἘ"): {
                    bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧἙ"): feature.name,
                    bstack1lllll1_opy_ (u"ࠪࡴࡦࡺࡨࠨἚ"): feature.filename,
                    bstack1lllll1_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩἛ"): feature.description
                },
                bstack1lllll1_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧἜ"): {
                    bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫἝ"): scenario.name
                },
                bstack1lllll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭἞"): steps,
                bstack1lllll1_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪ἟"): bstack11l11l11111_opy_(test)
            }
        )
    def bstack111111lllll_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨἠ"): self.hooks
        }
    def bstack111111lll11_opy_(self):
        if self.bstack1lll1111_opy_:
            return {
                bstack1lllll1_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩἡ"): self.bstack1lll1111_opy_
            }
        return {}
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def bstack11111l11l11_opy_(self):
        return {
            **super().bstack11111l11l11_opy_(),
            **self.bstack111111lll11_opy_()
        }
    def event_key(self):
        return bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ἢ")
class bstack1l111lll_opy_(bstack1l11l111_opy_):
    def __init__(self, hook_type, *args,bstack1lll1111_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111l111l1_opy_ = None
        self.bstack1lll1111_opy_ = bstack1lll1111_opy_
        super().__init__(*args, **kwargs, bstack11ll1lll1l_opy_=bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪἣ"))
    def bstack1l1l1lll_opy_(self):
        return self.hook_type
    def bstack11111l1l111_opy_(self):
        return {
            bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩἤ"): self.hook_type
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            **self.bstack11111l1l111_opy_()
        }
    def bstack11111l11l11_opy_(self):
        return {
            **super().bstack11111l11l11_opy_(),
            bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡ࡬ࡨࠬἥ"): self.bstack1l111l111l1_opy_,
            **self.bstack11111l1l111_opy_()
        }
    def event_key(self):
        return bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪἦ")
    def bstack11ll1l1l_opy_(self, bstack1l111l111l1_opy_):
        self.bstack1l111l111l1_opy_ = bstack1l111l111l1_opy_